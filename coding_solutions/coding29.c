/* Armstrong number is a number that is equal to the sum of cubes of its digits. For example 0, 1, 153, 370, 371 and 407 are the Armstrong numbers.*/
#include <stdio.h>
int main() {
    int num, originalNum, rem, result = 0;
    printf("Enter a three digit number: ");
    scanf("%d", &num);
    originalNum = num;

    while (originalNum != 0) {
       
        rem = originalNum % 10;
        
       result += rem * rem * rem;
        
       
       originalNum /= 10;
    }

    if (result == num)
        printf("%d is an Armstrong number.", num);
    else
        printf("%d is not an Armstrong number.", num);

    return 0;
}
