/* a program by raj upadhyay */

import java.util.*;

class TestClass{
	
  public static void main(String[] args){
		
    Scanner s=new Scanner(System.in);
		int total,n,n1,n2;
		total = s.nextInt();
		while(total > 0){
		int a1,b1,ans,c=0;
		  n1 = s.nextInt();
			n2 = s.nextInt();
			n = s.nextInt();
			
      if((n1!= 0))
				a1=n/n1;
			else
				a1=100;
			
      if((n2!=0))
				b1=n/n2;
			else
				b1=100;
			
      int a[]=new int [a1+1];
			int b[]=new int [b1+1];		
			
      for(int i=0;i<=a1;i++){
				a[i] = n1 * i; 
			}
			for(int i=0;i<=b1;i++){
				b[i] = n2 * i; 
			}
			for(int i=0;i<a.length;i++){
				for(int j=0;j<b.length;j++){
						ans=a[i]+b[j];
						if(ans == n){
							c++;
					}
				}
			}
		System.out.println(c);
		total--;
		}
	}
}
