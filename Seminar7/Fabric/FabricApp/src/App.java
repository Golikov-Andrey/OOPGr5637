import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.concurrent.ThreadLocalRandom;

import Fabric.GemGenerator;
import Fabric.GoldGenerator;
import Fabric.ItemGenerator;

public class App {
    public static void main(String[] args) throws Exception {
       ItemGenerator f1 = new GoldGenerator();
       f1.openReward();
       ItemGenerator f2 = new GemGenerator();
       f2.openReward();

       List<ItemGenerator> generatorList = new ArrayList<>();
       generatorList.add(f1);
       generatorList.add(f2);
       generatorList.add(new GoldGenerator());
       generatorList.add(new GoldGenerator());
       generatorList.add(new GoldGenerator());
       generatorList.add(new GoldGenerator());

       Random rnd = ThreadLocalRandom.current();

        
        for(int i =0;i<10;i++)
        {
            int index = rnd.nextInt(6);
            generatorList.get(index).openReward();
        }
    }
}
