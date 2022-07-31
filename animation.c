#include <stdio.h>
#include <stdlib.h>
#include <sys/ioctl.h> // ioctl, TIOCGWINSZ
#include <err.h>       // err
#include <fcntl.h>     // open
#include <unistd.h>    // close
#include <termios.h>


size_t* get_screen_size()
{
  size_t* result = malloc(sizeof(size_t) * 2);
  if(!result) err(1, "Memory Error");

  struct winsize ws;
  int fd;

  fd = open("/dev/tty", 0_RDWR);
  if(fd < 0 || ioctl(fd, TIOCGWINSZ, &ws) < 0) err(8, "/dev/tty");

  result[0] = ws.ws_row;
  result[1] = ws.ws_col;

  close(fd);

  return result;
}

int main(){

    // struct winsize w;
    // for (int i = 0;;i++){
        
    //     ioctl(STDOUT_FILENO, TIOCGWINSZ, &w);

    //     printf ("columns %d\n", w.ws_col);
    //     printf ("lines %d\n", w.ws_row);
    //     usleep(50000);
    //     printf("%s%d%s","\x1b[",2,"A");
    // }
    double array[] = get_screen_size();
    printf("%d",array[0]);
    // for (int i = 0;;i++){

        

    //     usleep(50000);
    //     printf("%s%d%s","\x1b[",frame_height+1,"A");
    // }
}