#include <unistd.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>
#include <errno.h>

#define BUFSIZE 20


void printfile() 
{
    char buf[BUFSIZE];
    int n;
    int fd;

    fd = open("sample.txt",O_RDONLY);
    /*
    n = read(fd,buf,BUFSIZE);
    write(1,buf,n);
    n = read(fd,buf,BUFSIZE);
    write(1,buf,n);
    n = read(fd,buf,BUFSIZE);
    write(1,buf,n);
    */

    printf("New Entry of Lseek \n" );

    lseek(fd,BUFSIZE*(-10),SEEK_END);
    n = read(fd,buf,BUFSIZE);
    write(1,buf,n);
/*
    lseek(fd,BUFSIZE*(-5),SEEK_END);
    n = read(fd,buf,BUFSIZE);
    write(1,buf,n);
*/
    lseek(fd,BUFSIZE*(2),SEEK_SET);
    n = read(fd,buf,BUFSIZE);
    write(1,buf,n);

    lseek(fd,BUFSIZE*(2),SEEK_CUR);
    n = read(fd,buf,BUFSIZE);
    write(1,buf,n);

/*    while((n=read(0,buf,BUFSIZE))>0)
    {
        write(1,buf,n);
    }
    */
}
int filecopy (int fd, int outfd)
{
    char buf[50];
    int fd1,fd2, n;

    fd1 = open("sample.text", O_RDONLY);
    fd2 = open("sample.text", O_RDONLY);

    n = read(fd1, buf, 10);
    write(STDOUT_FILENO, buf,n);


}

int main(int argc, char *argv[])

{
    
    printfile();
    return 0;
}