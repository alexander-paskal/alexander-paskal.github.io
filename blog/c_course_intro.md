# Motivation

I need to get really good at C programming. Why, you ask? Couple of reasons:

1. I want to write really high-performance simulations for reinforcement learning. Yes I could vectorize everything (as is common in many sims) and rely on massive gpu acceleration, but there are some tradeoffs here in terms of code and logic complexity that imo I don't want to be pigeonholed into.
2. I want to deeply understand everything that's happening at as low a level as I can on the computer. Ideally, i'll have intuition for how the commands I'm programming will be converted into and executed as machine code. Will I end up handrolling assembly? Maybe. But the more intuition for how things are being executed, the more i'll be able to anticipate performance pitfalls. 
3. Since I don't have a formal CS degree (ECE masters doesn't count, that was mostly robots and AI algos), I might finally feel like a "real" programmer. Doubtful, but conceivable.
4. In the age of AI, the people who have the deepest intuition about how programs run will both be the most capable of maximally leveraging the AI and the most capable of fixing it when it poops the bed.
5. Screw it, why not?



# Background


I have done some random stuff in C. I worked in C++ for 6 months at a robotics startup. I can edit code fine, I can read it ... ehh, passably. I can write it as needed. Especially in the age of AI, i can do fine if there's an existing structure in place and I can pattern match my way through. 

But I can make miracles happen in Python. I can speak that language fluently, and fully express myself without getting lost in translation. I can sit down and just code, and it works out (good to do some design first but that's not a language thing). I want the same with C. To be honest, I'd rather be better at C. Not C++, I hate the whole OOP paradigm as the default answer to "how do we organize our software". Casey Muratori has a really good thing about this [here](https://www.youtube.com/watch?v=tD5NrevFtbU&t=1s) as well as a longer lecture about the history of OOP, the types of problems it was originally intended to solve, and other paradigms that could have potentially taken its place [here](https://www.youtube.com/watch?v=wo84LFzx5nI). Besides, I want the most minimal level of abstraction here, so that I can make my own decisions about what levels of abstraction will actually serve me in doing different tasks. 

I'm comfortable with the syntax of C. I can struggle through some memory allocation with help. But the coding infrastructure? Project layout, profiling, compiling, debugging tools? Nope. Could I write you a web server with minimal assistance? Absolutely not. Super high performance, multi-threaded SIMD? Negative. Sockets? GUIs? Nada. That's the stuff I want to know. The ideal here is that when I'm done with this course (which i would expect to take 150-200 hours of focused effort), I will be able to take any common programming task that I might do in Python, and I will be able to do it in C without needing to ask general "how do I do this?" questions. Not only that, but I'll know how to make it run really FAST. Cause god dammit, I wanna go fast.  

# Approach

So, how to do this? Well, I could sit and grind coursera courses. But I might hurl myself from the roof of my apartment building from boredom. Plus, with those you get stuck in tutorial hell, and don't build robust knowledge that you can apply elsewhere. I could sit and work through a book like [Modern C](https://inria.hal.science/hal-02383654v2/file/modernC.pdf), but similar problems. My general thesis is that knowledge becomes skill through the application of that knowledge under diverse and ambiguous circumstances. In other words, not just being able to say **how** to do something, but **when** and **if** you should do something, and how you can adapt another approach to fit this circumstance. Not just blindly following recipes, but building intuition by glimpsing the timeless principles that underly them. That sort of thing only comes through making a bunch of crap. 

So, my approach in a nutshell is going to be that - make a bunch of crap.

But what to make? How do i scaffold, so i'm not diving into something way outside of my wheelhouse? How do I make sure the tasks I'm being asked to do aren't overly contrived so as to not require me to exercise useful skills? Well, not an easy answer there, so I turned to the AIs. First, I asked for a general taxonomy of the things I need to know to be generally competent at C. A summary of its response yields this roadmap:


1. Core Language & Mechanics
- Standards & Evolution: Differences between C99, C11, C17, and C23 (what to use and avoid).
- Memory Model: Stack vs. heap, memory layout (text, data, bss), pointer arithmetic, alignment, strict aliasing.
- Undefined Behavior (UB): Common traps (out-of-bounds, use-after-free, integer overflow, sequence points) and how to reason about UB.
- Type System: Integer promotion rules, implicit conversions, void*, const/volatile/restrict qualifiers.

2. Toolchains & Compilers
- Compilers: GCC, Clang, MSVC — options, optimization flags (-O2, -O3, -Os, -flto), warning levels (-Wall -Wextra -Wpedantic -Werror).
- Sanitizers: AddressSanitizer (ASan), UndefinedBehaviorSanitizer (UBSan), ThreadSanitizer (TSan), MemorySanitizer (MSan).
- Preprocessors & Linking: Macro pitfalls, conditional compilation, static (.a/.lib) vs. dynamic (.so/.dll) libraries, symbol visibility.

3. Build Systems & Package Management
- Build Tools: GNU Make, CMake, Meson, Ninja.
- Dependency Management: Integration strategies (submodules, pkg-config, Conan, vcpkg).

4. Debugging & Memory Inspection
- GDB / LLDB: Breakpoints, watchpoints, stack traces, inspecting memory/registers, core dumps.
- Memory Auditing: Valgrind (memcheck), visual leak detectors.

5. Profiling & Optimization
- Profiling Tools: perf, gprof, Valgrind (callgrind), FlameGraphs.
- Hardware Awareness: Cache locality, CPU instruction pipelines, branch prediction, SIMD/vectorization (AVX, NEON).

6. Concurrency & Parallelism
- Threads: POSIX Threads (pthreads), C11 <threads.h>.
- Synchronization: Mutexes, condition variables, read-write locks, semaphores.
- Atomics & Lock-Free: C11 <stdatomic.h>, memory ordering guarantees.
- Multiprocessing / GPU: fork/exec, OpenMP, CUDA/OpenCL integration.

7. Systems, Networking & I/O
- POSIX / System Calls: File descriptors, signals, process management.
- Networking: Berkeley Sockets (sys/socket.h), TCP/UDP, non-blocking I/O.
- I/O Multiplexing: select, poll, epoll (Linux), kqueue (BSD/macOS), io_uring.

8. Ecosystem & Common Domain Libraries
- Networking/Web: libcurl, libuv, libwebsockets, OpenSSL/mbedTLS.
- Data & Storage: SQLite, cJSON / yyjson.
- GUI & Graphics: SDL2/SDL3, GLFW, Raylib, cairo, GTK.
- Interoperability: FFI (Foreign Function Interface), binding C libraries to Python, Rust, or Node.js.


Now, is this complete? Hell if I know. But it looks like a pretty good starting point. Next I asked it to convert this into a set of 15 exercises that follow a sort of [spiral curriculum](https://en.wikipedia.org/wiki/Spiral_approach). The results are at the bottom of this file (since they're pretty long). 

Here's what my task is:

I'm going to sit down and work through these exercises.
I will use NO ai-generated code (I will only use them for answering generic C questions).
I will use the modern C book as an offline reference while I'm coding.
I will write an article post about each exercise, walking through the logic and bits of the code.
I will post functioning code up on the github.
AFTER I finish, I will ask Claude to rip my life apart with a PR review. These will be attached to a separate MD file but will NOT be incorporated into the code itself.


We'll see how it goes!


# Curriculum (AI from here on out)

This curriculum is designed as a spiral learning path to take you from foundational C mechanics to advanced systems architecture, low-level optimization, concurrent systems, and production tooling.

---

## Project 1: Dynamic Array & Custom Arena Allocator

Core Skills & Mechanics
- Pointer arithmetic, memory layout, structural byte alignment.
- Custom memory management paradigms vs. standard heap allocations.
- Fundamentals of build scripts (`Makefile`).

Functional Requirements
- **Dynamic Array (`vector_t`):**
  - Implement a generic, type-agnostic dynamic array using `void*`.
  - Core API: `vector_create`, `vector_push_back`, `vector_pop_back`, `vector_get`, `vector_shrink_to_fit`, and `vector_destroy`.
  - Amortized $O(1)$ growth policy (e.g., doubling strategy).
- **Arena Allocator (`arena_t`):**
  - Implement a contiguous block arena allocator (`arena_init`, `arena_alloc`, `arena_reset`, `arena_free`).
  - Require all dynamic array operations to accept an `arena_t*` handle for memory allocations rather than invoking `malloc`/`free` directly.
  - Enforce byte alignment (e.g., 8-byte or 16-byte aligned address boundaries).

 Performance & Tooling Constraints
- **Compiler Flags:** Clean compilation with `gcc -std=c11 -Wall -Wextra -Wpedantic -Werror`.
- **Sanitizers:** Zero errors under AddressSanitizer (`-fsanitize=address`) and LeakSanitizer (`-fsanitize=leak`).
- **Memory Inspection:** Zero dynamic memory leaks verified via `valgrind --tool=memcheck --leak-check=full`.

---

## Project 2: Robust Streaming Log Parser

 Core Skills & Mechanics
- File I/O buffering, non-destructive string parsing, state machines.
- Defensive programming, bounds checking, explicit error recovery.
- Compiler warnings and static analysis.

 Functional Requirements
- Parse massive line-oriented log files (e.g., Nginx access logs or syslog formats) without loading full files into memory.
- Use a fixed-size ring or chunk buffer to read streams incrementally.
- Implement an explicit finite state machine (FSM) to extract fields: `timestamp`, `log_level`, `source_ip`, and `message_payload`.
- Handle edge cases gracefully: truncated lines, malformed UTF-8, missing delimiters, or oversized tokens, without crashing or terminating execution prematurely.

 Performance & Tooling Constraints
- **Memory Footprint:** Fixed stack/heap memory consumption regardless of input file size (e.g., $\le 10\text{ MB}$ RSS for a $100\text{ GB}$ file).
- **Sanitizers:** Compile with UndefinedBehaviorSanitizer (`-fsanitize=undefined,bounds,integer`).
- **Static Analysis:** Zero findings using `clang-tidy` with checks enabled for `clang-analyzer-*` and `bugprone-*`.

---

## Project 3: Cache-Aligned Hash Map with Arena Backing

 Core Skills & Mechanics
- Hash table algorithms, collision resolution (open addressing, linear probing).
- Cache-line optimization, structure padding, alignment primitives.
- Modern build system configuration with CMake.

 Functional Requirements
- Implement a high-performance hash map using open addressing and linear probing.
- Support string/opaque byte keys and generic binary values.
- Back all bucket arrays and entry metadata strictly with the `arena_t` allocator from Project 1.
- Align key-value entries to 64-byte cache-line boundaries using standard specifiers (`alignas` or `_Alignas`).

 Performance & Tooling Constraints
- **Build System:** Transition from raw Makefiles to a modular `CMakeLists.txt` supporting Debug and Release targets.
- **Testing:** Comprehensive unit test suite using a lightweight test framework (e.g., `Unity` or a custom macro suite).
- **Cache Profiling:** Evaluate cache utilization with `valgrind --tool=cachegrind` to verify cache miss ratios.

---

## Project 4: Modular Library Packaging & Symbol Visibility

 Core Skills & Mechanics
- Binary artifacts: static libraries (`.a`), shared/dynamic libraries (`.so` / `.dylib`).
- Symbol exports, linkage attributes, ABI stability.
- Package discovery integration (`pkg-config`).

 Functional Requirements
- Refactor Projects 1–3 into a standalone distribution library (`libcore`).
- Structure source trees cleanly: `include/libcore/`, `src/`, `tests/`, `cmake/`.
- Manage public API header visibility: annotate public interfaces with visibility macros (`__attribute__((visibility("default")))`) and pass `-fvisibility=hidden` to suppress internal helper functions.
- Produce both static (`libcore.a`) and dynamic (`libcore.so`) build targets.

 Performance & Tooling Constraints
- **Distribution:** Generate a functional `libcore.pc` file during CMake configure stage.
- **Verification:** Inspect generated dynamic library symbol tables using `nm -D` or `readelf -s` to verify zero non-prefixed or internal leaking symbols.

---

## Project 5: Process Pipeline & Execution Engine

 Core Skills & Mechanics
- POSIX system call interface (`fork`, `execvp`, `pipe`, `dup2`, `waitpid`).
- Process lifecycle management, file descriptor tracking, signal handling.

 Functional Requirements
- Build a pipeline execution CLI tool capable of parsing and executing chained shell command pipelines (e.g., `cat file.txt | grep "ERROR" | wc -l`).
- Implement file descriptor redirection (`>`, `<`, `2>`).
- Implement robust signal handlers for `SIGINT`, `SIGTERM`, and `SIGCHLD` to prevent zombie processes and safely propagate cancellation across child processes.

 Performance & Tooling Constraints
- **Resource Auditing:** Verify clean descriptor cleanup across child process trees using `lsof` or by auditing `/proc/self/fd/`.
- **Error Handling:** Every system call return value must be checked with explicit handling for `EINTR`.

---

## Project 6: Multithreaded Work-Stealing Task Pool

 Core Skills & Mechanics
- POSIX Threads (`pthreads`), thread lifecycle management.
- Synchronization primitives: mutexes, condition variables, atomic flags.
- Task distribution architectures (work-stealing queues).

 Functional Requirements
- Build a thread pool that manages $N$ worker threads ($N = \text{hardware core count}$).
- Each worker thread must manage a local double-ended queue (deque) of function pointers and argument payloads.
- Implement task stealing: idle workers attempt to steal tasks from the tail of busier workers' queues when local queues are empty.
- Provide a blocking `threadpool_wait` and a thread-safe `threadpool_shutdown` procedure ensuring zero lost tasks.

 Performance & Tooling Constraints
- **Sanitizers:** Zero data races or synchronization defects under ThreadSanitizer (`-fsanitize=thread`).
- **Stress Testing:** Validate under high contention scenarios (e.g., 100,000 sub-millisecond atomic tasks).

---

## Project 7: Lock-Free SPSC Ring Buffer & SIMD Acceleration

 Core Skills & Mechanics
- C11 Atomics (`<stdatomic.h>`), explicit memory orderings (`acquire`/`release`).
- Cache coherency (false sharing prevention).
- Hardware vectorization via SIMD intrinsics (AVX2 / ARM NEON).

 Functional Requirements
- **Lock-Free Ring Buffer:**
  - Build a Single-Producer Single-Consumer (SPSC) circular queue.
  - Implement lock-free enqueue/dequeue using atomic index manipulations and explicit `memory_order_relaxed`, `memory_order_acquire`, and `memory_order_release` sematics.
  - Pad atomic indices to separate 64-byte boundaries to eliminate false sharing.
- **SIMD Processing:**
  - Implement a numeric stream-processing pipeline over queue entries using SIMD intrinsics (e.g., `_mm256_fmadd_ps` for AVX2 or `vmlaq_f32` for NEON).

 Performance & Tooling Constraints
- **Assembly Verification:** Inspect generated assembly output (`-S -masm=intel`) to verify vector unit usage and absence of implicit memory barriers.
- **Benchmarking:** Measure throughput vs. standard lock-based queues using CPU counter profiling (`perf stat`).

---

## Project 8: Non-Blocking Event-Driven HTTP/1.1 Server

 Core Skills & Mechanics
- Berkeley Sockets API, non-blocking I/O (`O_NONBLOCK`).
- OS I/O multiplexing primitives (`epoll` on Linux, `kqueue` on macOS/BSD).
- State-machine HTTP protocol parsing.

 Functional Requirements
- Construct an event-driven HTTP/1.1 server running on a single execution thread.
- Configure socket options correctly (`SO_REUSEADDR`, `TCP_NODELAY`).
- Use `epoll` or `kqueue` to manage state transitions across thousands of active client socket connections.
- Implement an explicit state-machine parser for HTTP requests.
- Serve static files directly using high-performance zero-copy system calls (`sendfile` on Linux / `out_fd` on BSD).

 Performance & Tooling Constraints
- **Load Testing:** Achieve high concurrency throughput validated via benchmarking tools (`wrk -t12 -c400 -d30s`).
- **Resource Limits:** Validate descriptor limits and memory stability under starvation conditions.

---

## Project 9: Embedded Key-Value Store (LSM-Tree)

 Core Skills & Mechanics
- Persistent storage architecture, write-ahead logs (WAL).
- Memory-mapped file I/O (`mmap`, `msync`).
- Structured binary encoding and file compaction algorithms.

 Functional Requirements
- Build an embedded Log-Structured Merge-tree (LSM-tree) engine.
- **MemTable:** Accumulate in-memory writes in the hash map structure (Project 3) backed by an append-only WAL on disk.
- **SSTables:** Flush full MemTables to immutable sorted string tables (SSTables) on disk.
- Implement `get(key)` and `put(key, value)` primitives: reads query MemTable first, falling back to memory-mapped (`mmap`) SSTable files.
- Implement a background compaction pass to merge overlapping SSTables and remove tombstones.

 Performance & Tooling Constraints
- **I/O Profiling:** Measure storage I/O bottlenecks and page faults using `perf stat -e page-faults` and Callgrind (`valgrind --tool=callgrind`).

---

## Project 10: High-Throughput Asynchronous Engine (`io_uring` / `libuv`)

 Core Skills & Mechanics
- Modern kernel async interfaces (`io_uring`) or event abstraction layers (`libuv`).
- Zero-copy ring submission paradigms.
- High-performance asynchronous file and network pipelines.

 Functional Requirements
- Refactor the I/O core of Projects 8 and 9 to leverage Linux `io_uring` (or cross-platform `libuv`).
- Implement ring submission queue entry (SQE) and completion queue entry (CQE) batch processing loops.
- Implement registered file descriptors and fixed memory buffers to minimize kernel-space transitions.

 Performance & Tooling Constraints
- **Profiling:** Generate CPU and call-stack FlameGraphs (`perf script | stackcollapse-perf.pl | flamegraph.pl`).
- **Metrics:** Compare latency, throughput, and system call overhead directly against the Project 8 `epoll` baseline.

---

## Project 11: Real-Time Audio Synthesizer or Engine Subsystem

 Core Skills & Mechanics
- Integration of third-party multimedia libraries (`SDL2`/`SDL3`, `PortAudio`, `Raylib`).
- Real-time performance constraints, non-blocking real-time callbacks.
- Dependency management with CMake `FetchContent` or package managers (`vcpkg`/`conan`).

 Functional Requirements
- Build a real-time system: a multi-oscillator subtractive audio synthesizer or a 2D particle/rendering system.
- Integration via modern build dependency management (e.g., `vcpkg` or CMake `FetchContent`).
- **Strict Real-Time Constraints:** The main audio processing loop or render loop must execute within hard time bounds ($\le 5\text{ ms}$ buffer windows for audio or $\le 16.6\text{ ms}$ for 60 FPS frame rates).
- **Zero Allocations Rule:** Strictly forbid heap allocations (`malloc`, `free`), file operations, or blocking synchronization primitives within the real-time callback loop.

 Performance & Tooling Constraints
- **Frame/Audio Audit:** Monitor frame pacing stability and eliminate audio buffer under-runs (xruns) using high-resolution timers (`clock_gettime(CLOCK_MONOTONIC)`).

---

## Project 12: TLS-Encrypted Asynchronous Proxy

 Core Skills & Mechanics
- Applied cryptography integration (`OpenSSL` or `mbedTLS`).
- TLS handshakes over non-blocking sockets.
- Network proxying and stream forwarding.

 Functional Requirements
- Construct a forward/reverse network proxy wrapping plain socket streams with TLS encryption.
- Integrate OpenSSL (`libssl`/`libcrypto`) or mbedTLS.
- Process non-blocking TLS state transitions (`SSL_ERROR_WANT_READ`, `SSL_ERROR_WANT_WRITE`) seamlessly within your event loop (Project 8/10).
- Validate X.509 certificates, hostname verification, and negotiate modern TLS versions (TLS 1.2/1.3).

 Performance & Tooling Constraints
- **Verification:** Validate proxy security parameters and certificate chains using `openssl s_client` and `curl -v`.
- **Leak Auditing:** Ensure zero cryptographic context or memory leaks upon abrupt client disconnects.

---

## Project 13: Multi-Language C Foreign Function Interface (FFI)

 Core Skills & Mechanics
- C Application Binary Interface (ABI), calling conventions (`cdecl`).
- Language bindings: Python (`ctypes`/`cffi`), Rust (`bindgen`), or Node.js (`N-API`).
- Cross-language memory safety and ownership boundaries.

 Functional Requirements
- Expose the C core library (`libcore` or LSM key-value store) to high-level language environments.
- Provide idiomatic bindings for Python or Rust.
- Manage memory ownership explicitly: define clear boundaries for which runtime allocates, owns, and frees memory structures.
- Implement exception and error translation from C error status codes into native language exceptions or Result types.

 Performance & Tooling Constraints
- **Validation:** Automated test suites running cross-language integration scripts verifying zero memory leaks across the FFI boundary.

---

## Project 14: Dynamic Binary Instrumentation & Symbol Resolver

 Core Skills & Mechanics
- Executable and Linkable Format (ELF) internal structures (`Elf64_Ehdr`, `Elf64_Shdr`, `Elf64_Sym`).
- Dynamic process inspection via POSIX `ptrace` system calls.
- Address-to-symbol resolution.

 Functional Requirements
- Build a command-line utility that inspects and traces live target binaries.
- Parse ELF file headers directly from disk to locate dynamic symbol tables (`.dynsym`, `.strtab`).
- Attach to running processes using `ptrace(PTRACE_ATTACH, ...)` or Linux eBPF probes.
- Intercept function entries, inspect CPU register contents (e.g., `user_regs_struct`), and output real-time function invocation counts and execution durations.

 Performance & Tooling Constraints
- **Accuracy:** Cross-validate resolved addresses and symbol offsets against output from `gdb`, `objdump -T`, and `readelf -s`.

---

## Project 15: Production-Grade Distributed In-Memory Cache

 Core Skills & Mechanics
- Full-system integration: network protocols, storage, concurrency, build automation.
- Protocol parsing (e.g., RESP - Redis Serialization Protocol).
- Build matrices, cross-compilation, CI/CD pipelines.

 Functional Requirements
- Build a multithreaded, clustered in-memory caching engine (subset of Redis / RESP protocol).
- **Networking:** Asynchronous I/O event loops handling concurrent client socket pools.
- **Concurrency Model:** Multi-threaded worker queues driven by lock-free SPSC ring buffers (Project 7).
- **Persistence:** Async snapshots and append-only log execution driven by LSM engine subsystems (Project 9).
- **Storage:** Internal key-value stores built upon cache-aligned, arena-allocated hash maps (Project 3).
- **Build System:** Production Meson or CMake build system with options for Release, Debug, Sanitizer, and Static analysis builds.

 Performance & Tooling Constraints
- **Build Optimization:** Compile release builds with `-O3 -flto` (Link-Time Optimization) and `-march=native`.
- **Stress Suite:** Zero defects under 24-hour continuous stress testing with ASan, TSan, and Valgrind enabled.
- **CI Pipeline:** Fully automated pipeline building across compilers (GCC, Clang) and execution environments.















