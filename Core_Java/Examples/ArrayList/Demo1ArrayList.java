package ArrayList;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class Demo1ArrayList {
    public static void main(String[] args) {
        List<Integer> lt = new ArrayList<Integer>();
        lt.add(20);
        lt.add(30);
        lt.add(10);
        lt.add(40);
        System.out.println(lt);
        int sum=0;
        for(int ele : lt) {
            System.out.println(ele);
            sum=sum+ele;
        }
        System.out.println("Added value = "+sum);
        Iterator<Integer> itr = lt.iterator();
        while(itr.hasNext()) {
            int x = itr.next();
            System.out.println(x);
            if(x < 20)
                itr.remove();
        }
        System.out.println(lt);
        //lambda Expression
        /*void myfn(int e) {
            System.out.println(e);
        }*/
        /**
         * return type -- NA
         * function name -- NA Anonymous functions
         * () input paraters -- yes but without data types
         * -> -- its a lambda expression
         * {} -- function body : yes
         */
        System.out.println("Using Lambda Expression");
        lt.forEach((ele)->{System.out.println(ele);});
    }
}    
