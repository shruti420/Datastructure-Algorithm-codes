import java.util.*;
import java.io.*;

import java.util.Scanner;

public class Prg2 {
     public static void main(String[] args) {
           Scanner scanner= new Scanner(System.in);
           int n=scanner.nextInt();
           long[] array = new long[n];
           for(int i=0;i<n;i++)
                array[i]=scanner.nextInt();
           long result= MaxPairWiseProduct(array);
           System.out.println(result);
     }   
static long MaxPairWiseProduct(long[] array){
           int n=array.length;
           int index1=-1, index2=-1;
           for(int i=0;i<n;i++)
                if((index1==-1)|| (array[i]>array[index1]))
                index1=i;
           for(int j=0;j<n;j++)
                if((j != index1) &&((index2==-1)||                         (array[j]>array[index2])))
                index2=j;
           return (long)(array[index1]* array[index2]);
           }
     }
