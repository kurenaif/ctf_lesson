
import java.util.ArrayList;
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        Random random = new Random();
        ArrayList<Integer> outputs = new ArrayList<Integer>();
        ArrayList<Integer> values = new ArrayList<Integer>();

        for(int i=0;i<5;i++){
            outputs.add(random.nextInt(1<<16));
        }

        for(int i=0;i<100;i++){
            values.add(random.nextInt());
        }

        System.out.println("given: "+ outputs.get(0).toString() + " " + outputs.get(1).toString() + " " + outputs.get(2).toString() + " " + outputs.get(3).toString() + " " + outputs.get(4).toString());
        System.out.println("next: " + values.toString());

    }
}
