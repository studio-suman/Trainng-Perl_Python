#include <unistd.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>
#include <errno.h>

int k = 100;

void forParent() 
{
printf("P Line - %d - in process PID %d and PPID %d k = %d \n",
__LINE__, getpid(),getppid(),k++);

fork();
printf("P Line - %d - in process PID %d and PPID %d k = %d \n",
__LINE__, getpid(),getppid(),k++);

printf("P Line - %d in process PID %d and PPID %d k = %d \n",
__LINE__, getpid(),getppid(),k++);

printf("P Line - %d in process PID %d and PPID %d k = %d \n",
__LINE__, getpid(),getppid(),k++);

}

void forChild() 
{
printf("C Line - %d - in process PID %d and PPID %d k = %d \n",
__LINE__, getpid(),getppid(),k++);

fork();
printf("C Line - %d - in process PID %d and PPID %d k = %d \n",
__LINE__, getpid(),getppid(),k++);

printf("C Line - %d in process PID %d and PPID %d k = %d \n",
__LINE__, getpid(),getppid(),k++);

printf("C Line - %d in process PID %d and PPID %d k = %d \n",
__LINE__, getpid(),getppid(),k++);

}

int main()
{
    int pid;
    printf("P Line - %d in process PID %d and PPID %d k = %d \n",
__LINE__, getpid(),getppid(),k++);
    pid = fork();
    printf("pid = %d\n",pid);
    if(pid == 0) {
        forChild();
    }
    else {
        forParent();
    }
    
    sleep(2);

}