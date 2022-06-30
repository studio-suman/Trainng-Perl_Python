package Introduction;

public class Exer1_2 {
    public static void main(String[] args) {
        int arr[] = {3,6,12,7,4,-34,67,23,98,6};
        int max = arr[0];
        int min = Integer.MAX_VALUE;
        int sum = 0;
        for(int ele : arr) {
            if(ele > max) {
                max= ele;
            }
            if(ele < min) {
                min=ele;
            }
            sum+=ele;
        }
        System.out.println("Max = "+max);
        System.out.println("Min = "+min);
        System.out.println("Sum = "+sum);
    }
}