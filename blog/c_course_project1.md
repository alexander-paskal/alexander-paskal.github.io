# Project 1: Dynamic Array & Custom Arena Allocator

## Instructions

### Core Skills & Mechanics
- Pointer arithmetic, memory layout, structural byte alignment.
- Custom memory management paradigms vs. standard heap allocations.
- Fundamentals of build scripts (`Makefile`).

### Functional Requirements
- **Dynamic Array (`vector_t`):**
  - Implement a generic, type-agnostic dynamic array using `void*`.
  - Core API: `vector_create`, `vector_push_back`, `vector_pop_back`, `vector_get`, `vector_shrink_to_fit`, and `vector_destroy`.
  - Amortized $O(1)$ growth policy (e.g., doubling strategy).
- **Arena Allocator (`arena_t`):**
  - Implement a contiguous block arena allocator (`arena_init`, `arena_alloc`, `arena_reset`, `arena_free`).
  - Require all dynamic array operations to accept an `arena_t*` handle for memory allocations rather than invoking `malloc`/`free` directly.
  
### Performance & Tooling Constraints
- **Compiler Flags:** Clean compilation with `gcc -std=c11 -Wall -Wextra -Wpedantic -Werror`.
- **Sanitizers:** Zero errors under AddressSanitizer (`-fsanitize=address`) and LeakSanitizer (`-fsanitize=leak`).
- **Memory Inspection:** Zero dynamic memory leaks verified via `valgrind --tool=memcheck --leak-check=full`.


# Implementing the vector

Alright so what was the point of this? Basically, in c++ we have a templated vector class. 
I've used that before and its not so bad. But in C, we don't have templates - so we have to write this by hand.

It's an interesting concept, especially coming from a python background: how do we make a function agnostic to a
 data structure? Well, obviously, we have to parametrize it. So the question then becomes, what parameters adequately
 describe a data structure? In this case, the only one we REALLY care about is the size of the data structure,
 since we need to know how much data we have to move our pointer by on each push/pop.

 So the essence of this ends up looking like:

```c
void *vector_push_back(
    size_t data_size,
    size_t capacity
);
```

where I basically tell vector how many bytes each "unit" of data is actually going
to take up. In return, it just gives me back a pointer to where that memory starts.

# Adjusting my Mental Model

Coming from a python background, I don't think almost at all about how much memory data takes up.
The places where I do are basically:
- doing machine learning when I need to worry about stuffing everything into a GPU
- when i'm saving / loading a file and its taking forever

Contrary to the common view, I DO think very much about performance. Typically, this looks like
thinking through what computations are being performend, the big O complexity of them, and
how i can reduce the runtime complexity or leverage some form of caching when possible.

C is simultaneously more specific and simpler - I'm not thinking at the object scale anymore, but
rather at the byte level. Everything I'm doing is just playing with what bytes go where and how I 
can keep track of their addresses. Personally I like it a lot, cause it forces you to really understand
what the hell you're doing and think through it to an extreme degree.

# Reevaluating what "performance" means

The typical Python programmer, when you ask them about why C programs run faster than Python, will likely
respond with something like "well C is compiled and there's no garbage collection". And this is very true.
However, it's not just that. You just simply don't code the same. You don't think the same. You think much
more critically about what your actual data is, and what you need and what you don't. The result is just
much leaner, simpler approaches to solving problems (at least at this micro scale that I'm currently on)

# Implementing the arena allocator

The vector implementation was the more difficult one, particularly due to just wrapping my head around
the pointer syntax. For example, what the hell even is this?

```c
int count = *((int *)array + 1);
```

Developing the capacity to read the syntax CLOSELY took a second (and frankly is still a work in progress). 
The arena implementation was much simpler to do, but conceptually a little more foreign. I've worked in C++,
I'm accustomed to using templated types. I've used similar patterns in python, so that wasn't a huge issue. 
However, designing a custom allocator was a little odd - it took my brain a second to decouple the vector
expand operation from the initial arena allocation.

However, it's a great example of a fundamental principle of computing - one larger, more expensive operation 
up to reduce cost throughout the lifecycle of the program.

The whole implementation ended up being quite simple:

```c
#include "arena.h"
#include <stdlib.h>
#include <stdio.h>


Arena arena_init(
    size_t capacity
) {
    char *buffer = malloc(capacity);
    Arena arena = {
        .buffer = buffer,
        .capacity = capacity,
        .offset = 0
    };
    return arena;
}


void *arena_alloc(
    Arena *a,
    size_t size
) {
    char *data_buffer = a->buffer + a->offset;
    a->offset += size;

    if (a->offset > a->capacity){
        // implement wrap around
        puts("FUUUUUUUCCCCKKKKKKKKK");
        a->offset -= a->capacity;
    }

    // will prob segfault if they write to something that triggers the wrap
    return data_buffer;
}

void arena_reset(
    Arena *a
){
    a->offset = 0;
}

void arena_free(
    Arena *a
) {
    free(a->buffer);
    a->buffer = NULL;
    a->capacity = 0;
    a->offset = 0;
}
```

The wrap-around is broken, I know, but i got bored and want to progress onto the next project to continue the journey. 

Onwards and upwards!