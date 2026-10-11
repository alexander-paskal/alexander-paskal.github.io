# On AI and Software Burnout

I can no longer count on my fingers the number of people I personally know who have recently told me that they are burnt out on software. These people are all very motivated, very capable, and have throughout what I have seen of their careers taken great pride in bringing a level of craftsmanship to their work. I myself have felt this as well.

Most, if not all, of them have explicitly called out the increasing ubiquity of AI and the (ostensibly inevitable) consequence of getting further and further away from the actual process of coding. Programming (which I will define here as the task of designing an algorithm that manipulates data on a computer in order to produce a desired effect, and implementing that algorithm in a programming language) has been, for me and many other engineers, a primary source of creative and intellectual expression and a wellspring of deep satisfaction.

In this article I hope to dig into:
- What makes conventional programming so satisfying for so many people
- What agentic tooling strips from that process

In a follow-up article I will touch on:
- The fundamental tension at play that makes this challenging to navigate
- How we can hope to find some sort of 80/20 split so that we can enjoy the job again


## Why Is Programming Fun?

"Fun" is not necessarily the right word, for coding can at times definitely feel like being in a toxic relationship. But once you get your feet under you and have a deep familiarity with a language and the set of tools it avails, it is undeniably addictive and can be extremely rewarding. Why is this? I believe it is because it incorporates the following:
- Deep decision making
- Skill progression
- Working memory utilization
- Struggle-and-succeed loops

### Deep Decision Making

Decision making is the process of assessing the current state of something, defining a vision of a future state, and choosing an action that will take you in the direction of that future state. What I mean by "deep" is essentially a description of the granularity of those decisions. Shallow decision making might be the high-level direction you want to take a project in. Deep decision making will encompass that high-level vision as well as lower-level design tradeoffs, and even further down into the core implementation details. I believe it is generally a fair statement to say that the deeper the level of decision making involved in a project, the more satisfaction can be derived from the achievement of the vision of that project.

### Skill Progression

Skill progression here includes both the increased set of knowledge and the increased capacity to bring that knowledge to bear in order to achieve a desired effect. It can span from learning a new language or framework, to acquiring a deeper understanding of low-level computer operations, to getting better at software design, to even getting snappier with Vim commands. The feeling of growing more "powerful" is core to what it means to be a programmer, and there is a tremendous amount of satisfaction when you are able to flex these skills that you've worked so hard to acquire in the process of creating something that you otherwise would not have been able to.

### Working Memory Utilization

Programming as a task requires you to develop a (sometimes very detailed) mental model of the data structures and algorithms at play, to maintain this mental model while you reason counterfactually about what modifications might bring you closer to your goal, and to explore it in the abstract while you consider possible unforeseen consequences of the changes you are considering. There is a direct correlation between how challenging the program is to reason about and the amount of satisfaction to be derived from ideating and correctly implementing a modification to the program.

### Struggle-and-Succeed Loops

At its core, the task of programming is one of delivering effort into a program and then being rewarded for that effort by seeing the program run as expected. There is a reward to be had, but in order to collect that reward, you have to put in the effort.

### In a Sentence

Succinctly, programming is the process of defining a vision of a program, constructing a mental model of what that program would look like, and leveraging hard-earned skills to reason about, decide on, and implement that vision in code at every level of abstraction.


## What Agentic Coding Strips from This Process

Agentic coding dismantles these pillars of satisfaction in an almost systematic way. Concretely:
- **Deep decision making.** Agents make all of the low-level decisions for you. You decide the high-level approach, and they make all of the fine details work. Often, they will even decide the high-level approach, and you are only making decisions about what the end product is supposed to look like. That feeling of high-to-low comprehension and seeing the full picture down to the tiniest detail is inherently degraded, and often just completely destroyed, when working with agents.
- **Skill progression.** Because the agents know everything, you don't NEED to know anything, at least in the short term when turning around a specific feature. There's certainly an argument to be made that more skilled programmers are more productive, both in the short term and (considerably more so) in the long term. However, generally speaking, if there is a gap between your skills and knowledge as a programmer and what the task you are intending to accomplish requires, it is completely invisible when using agents. There is no more flexing of the skills you've worked so hard to acquire. Even more tragically, there's no more skill development. While relying on agents for implementations, you will not get better as a programmer. You may gain more general awareness of what's out there in terms of technologies, but you will not be forced to learn these things at an implementation level, and thus they will not stick.
- **Working memory utilization.** Purely with respect to modifying code, there is no requirement for you to load the mental model of the program into your brain when you are using agents. You can be completely unaware of its internals and be every bit as productive (again, in the short term). The cognitive challenge of programming is completely gone.
- **Struggle-and-succeed loops.** This may be the only pillar of those enumerated that still survives somewhat, as there can certainly be a struggle when using agents that leads to satisfaction when they finally get it right (thanks to your careful prompting). However, that struggle feels far less *personal* to us, and as a result the success feels less personal and therefore less satisfying.

## In Conclusion

The benefits of agents in terms of short-term productivity are, frankly, immeasurable. For all intents and purposes, the minute-to-minute tasks of actually implementing changes to code have been modified. However, the costs of this are very real. I believe that there are real long-term productivity costs, and I will speak on those in a future post. That cost is still up for debate; what's not up for debate, in my opinion, is the tidal wave of ennui that is rippling across the software industry and causing skilled craftsmen to seriously consider whether this field is for them.

In my next post on this topic I will dig into the core tensions that define how we use agents, and give my thoughts on how we can find a way to retain the massive boost they provide without losing our love of the game in the process.
