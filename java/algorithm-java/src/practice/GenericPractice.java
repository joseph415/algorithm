package practice;

import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

public class GenericPractice {
    public static void main(String[] args) {
        System.out.println("");
    }

    public <T> List<T>[] a (List<T>[] a){
        Object[] b = a;
        Integer[] tt = new Integer[1];
        b[0] = tt;

        Map<String,Integer> treeMap = new TreeMap<>();
        return a;
    }
}
