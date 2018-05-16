/*package whatever //do not write package name here */

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
	
	public static void printArr(int arr[]){
		for(int i = 0; i < arr.length-1;i++)
			System.out.print(arr[i]+" ");
		System.out.print(arr[arr.length-1]);
		System.out.println();
	}
	
	public static void swap(int arr[], int i, int j)
	{
		int temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;
	}
	
	public static void sortarr(int[]a)
	{
		//Bubble sort the array
		// a1 a2 a3 a4 a5 a6
		for(int i = 0; i< a.length;i++)
			for(int j = 0; j < a.length-1-i;j++)
				if(a[j] > a[j+1]) 
					swap(a,j,j+1);
		
	}
	
	public static int[] rearrange(int a[]){
		//System.out.println("array before sorting:");
		//printArr(a);
		//sort the array first 
		sortarr(a);
		//System.out.println("array after sorting:");
		//printArr(a);
		int []b = new int[a.length];
		int pos; 
		float k=1.0F;
		int mid = (a.length-1)/2;
		//populate the b array with pendulum position mapping
		
		//base case
		b[mid] = a[0]; //first element goes to the mid
		
		for(int i = 1; i < a.length; i++){
			//index calculation
			pos = mid + ((i % 2 == 0)?-(int)k:(int)k);
			//element placement
			if( pos >= 0 && pos < a.length)
				b[pos] = a[i];
			k+=0.5;
			
		}
		
		
	 return b;	 
	}
	
	public static void main (String[] args) {
		Scanner s = new Scanner(System.in);
		
		int t = s.nextInt();
		int n;
		int a[];
		/*
		System.out.println("Input enter the String: ");
		String input = s.nextLine();
		
		System.out.println("You Entered This :" + input);*/
		
		
		for(int i=1; i<=t; i++){
			n = s.nextInt();
			a = new int[n];
			for(int j = 0; j<n ; j++){
				//Form the array / LL here
				a[j] = s.nextInt();
			}
			
			//do the transformation here
			int b[] = rearrange(a);
			
			//print ? etc
			//System.out.println("After rearrangement:");
			printArr(b);
			
			
			//reset the array/LL here
			a=null;b=null;
		}
	
		
		
		return;
	}
}