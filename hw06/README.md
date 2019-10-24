## HW6 README  
The purpose of this homework was to get some experience working with Real-time kernels. The start of this homework was to watch a video by Julia Cartwright and answer some questions. The answers to those questions are below:  
1. Julia Cartwright works at National Instruments  
2. The OS scheduler will optimize for the worst case scenerio latency
3. Mixed criticallity is when a system has a real time and bounded latency requirements and then non-time critical tasks  
4. The drivers can be shared and in that case the RT tasks and non-RT tasks can interfere with each other  
5. The delta represents latency between the event and the application  
6. Time difference between projected and actual sleep time  
7. The Cyclictest between preempt and preempt_rt  
8. Dispatch: Time from interrupt firing to the event to be woken up. Scheduling: Time for the woke up event to be scheduled  
9. A method of scheduling interrupts for non-RT  
10. a non-critical IRQ being handled  
11. Because it has a higher priority than the non-critical IRQ, so the IRQ is suspended and the external event is handled by the system sooner  

The next part of the homework was to run a stressful program in a RT kernel and a non-RT kernel and plot the difference in a cyclictest plot. The non-RT histogram is called 'nort.hist' and the RT histogram is called 'rt.hist'. The cyclictest plot is called out.png and can be displayed with:  
> xdg-open out.png  

Finally, the stressful program run during these tests was:  
> stress -c 1 -i 1 -m 1  
