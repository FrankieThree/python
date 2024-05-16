// Name: Norman Cook
// Date: 05/01/2020
// Description: Solving the dining philosopher problem with pthreads

#include <pthread.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

void * thread_function(void * arg);

int times_to_eat;
int num_threads;
pthread_mutex_t chop_sticks[32];
char start = 0;

int main(int argc, char * argv[])
{
    if (argc != 3)
    {
      printf("invalid args\n");
      exit(1);
    }

    // variables
    times_to_eat = atoi(argv[1]);
    num_threads = atoi(argv[2]);
    int philo_id[32];

    int times_eaten[num_threads];
    pthread_t thread_id[num_threads];

    int i, j;
    printf("About to init mutex\n");
    // create the mutex locks
    for(i=0;i<num_threads;i++)
    {
        //chop_sticks[i] = PTHREAD_MUTEX_INITIALIZER;
        pthread_mutex_init(&chop_sticks[i], NULL);
        continue;
    }

    // create the number of philosophers that the user inputed
    for(i=0;i<num_threads;i++)
    {
        philo_id[i] = i;
        pthread_create(&thread_id[i], NULL, &thread_function, &philo_id[i]);
        //printf("Philosopher %d is thinking...\n",i+1);
    }
    start = 1;

    // wait for the philosophers to finish
    for(j=0;j<num_threads;j++)
    {
        pthread_join(thread_id[j],NULL);
    }
}

void * thread_function(void * arg)
{
    int philo_id = *((int *) arg);
    for(int i=0;i<times_to_eat;i++) {
        printf("Philosopher %d is thinking...\n", philo_id+1);
        sleep(2);

        // even number philosopher takes first a right chopstick
        if (philo_id % 2 == 0) {
          if (philo_id == 0) {
            // for philosopher 1 the right chopstick is 0 and the left is 4
            pthread_mutex_lock(&chop_sticks[philo_id]);
            pthread_mutex_lock(&chop_sticks[num_threads]);
            printf("Philosopher %d is eating...\n", philo_id+1);
            sleep(3);
            pthread_mutex_unlock(&chop_sticks[0]);
            pthread_mutex_unlock(&chop_sticks[num_threads]);
          } else {
            // for philosopher 3 the right chopstick is 2 and the left is 1
            pthread_mutex_lock(&chop_sticks[philo_id]);
            pthread_mutex_lock(&chop_sticks[philo_id-1]);
            printf("Philosopher %d is eating...\n", philo_id+1);
            sleep(3);
            pthread_mutex_unlock(&chop_sticks[philo_id]);
            pthread_mutex_unlock(&chop_sticks[philo_id-1]);
          }
        }
        // odd number phiosopher takes first a left chopstick
        else {
          if (philo_id == 0) {
            // for philosopher 1 the right chopstick is 0 and the left is 4
            pthread_mutex_lock(&chop_sticks[num_threads]);
            pthread_mutex_lock(&chop_sticks[0]);
            printf("Philosopher %d is eating...\n", philo_id+1);
            sleep(3);
            pthread_mutex_unlock(&chop_sticks[num_threads]);
            pthread_mutex_unlock(&chop_sticks[0]);
          } else {
            // for philosopher 3 the right chopstick is 2 and the left is 1
            pthread_mutex_lock(&chop_sticks[philo_id-1]);
            pthread_mutex_lock(&chop_sticks[philo_id]);
            printf("Philosopher %d is eating...\n", philo_id+1);
            sleep(3);
            pthread_mutex_unlock(&chop_sticks[philo_id-1]);
            pthread_mutex_unlock(&chop_sticks[philo_id]);
          }
        }
    }
    printf("Philosopher %d finished.\n", philo_id+1);
    return NULL;
}
