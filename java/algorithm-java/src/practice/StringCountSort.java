package practice;

import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

import jdk.internal.org.objectweb.asm.commons.StaticInitMerger;

public class StringCountSort {
    public static void main(String[] args) {

        String test = "bbbbaaaacc";

        Map<Character,Integer> hashMap = new HashMap<>();
        for (int i = 0; i < test.length(); i++) {
            hashMap.putIfAbsent(test.charAt(i), 0);
            hashMap.put(test.charAt(i), hashMap.get(test.charAt(i)) + 1);
        }

        final List<Character> collect = hashMap.entrySet().stream()
                .sorted((o1, o2) -> {
                    if(o1.getValue().equals(o2.getValue())){
                        return o1.getKey().compareTo(o2.getKey());
                    }
                    return o1.getValue().compareTo(o2.getValue());
                })
                // .sorted(Comparator.comparing(Map.Entry::getValue))
                .map(Map.Entry::getKey)
                .collect(Collectors.toList());

        StringBuilder stringBuilder = new StringBuilder();
        for(Character c: collect){
            Integer count = hashMap.get(c);
            for (int i = 0; i < count; i++) {
                stringBuilder.append(c);
            }
        }
        System.out.println(stringBuilder);
    }
}
