#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>

#define FLAGSIZE_MAX 64

char flag[FLAGSIZE_MAX];

void sigsegv_handler(int sig) {
  fprintf(stderr, "%s\n", flag);
  fflush(stderr);
  exit(1);
}

void vuln(char *input){
  char buf[64];
  printf("Input: ");
  fflush(stdout);
  fgets(buf, 128, stdin);
  printf("Input received: %s\n", buf);
  fflush(stdout);
  return;
}

int main(int argc, char **argv){
 
  FILE *f = fopen("/opt/flag.txt","r");
  if (f == NULL) {
    perror("Could not open flag file: ");
    exit(0);
  }
  fgets(flag,FLAGSIZE_MAX,f);                                                                                              
  signal(SIGSEGV, sigsegv_handler);                                                                                                                                                                                     
  vuln(argv[1]);                                                                                                                                                                                                                                                                                             
  return 0;                                                                                                                
}      
