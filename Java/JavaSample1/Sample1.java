import java.util.Map;
import java.util.stream.Collector;
import java.util.stream.Collectors;
import java.util.HashMap;
import java.util.List;
import java.util.Collections;

public class Sample1{
    public static void main(String[] args){
        Map<String, String> map = new HashMap<String, String>();
        map.put("A1", "a3");
        map.put("A3", "a2");
        map.put("A2", "a4");
        map.put("B1", "b3");
        map.put("B3", "b2");
        map.put("B2", "b4");
        List<String> list = map.entrySet().stream().sorted(Map.Entry.comparingByValue()).map(e -> e.getKey()).collect(Collectors.toList());
        System.out.println(list);
    }
}