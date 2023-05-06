package jav.abinitio;

import jav.AdjacencyList;
import java.util.Scanner;

public class AbInitio {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int V = in.nextInt();
        int E = in.nextInt();
        int Q = in.nextInt();
        in.nextLine();
        AdjacencyList map = new AdjacencyList(V);
        for(int e = 0; e < E; e++){
            map.addEdge(in.nextInt(), in.nextInt());
            in.nextLine();
        }
        // System.err.println(map);
        for(int q = 0; q < Q; q++){
            String[] query=in.nextLine().split(" ");
            switch(Integer.parseInt(query[0])){
                case 1:
                    map.addNode();
                    break;
                case 2:
                    map.addEdge(Integer.parseInt(query[1]), Integer.parseInt(query[2]));
                    break;
                case 3:
                    map.delEdges(Integer.parseInt(query[1]));
                    break;
                case 4:
                    map.delEdge(Integer.parseInt(query[1]), Integer.parseInt(query[2]));
                    break;
                case 5:
                    map.flip();
                    break;
                case 6:
                    map.invert();
                    break;
            }
            // String qy = "";
            // for(String s : query){qy+=s+" ";}
            // System.err.println(qy+map);
        }
        map.rectify(true);
        int x = map.nodeCount();
        System.out.println(x);
        for(int i = 0; i < x; i++){ System.out.println(map.nodeHash(i)); }
        in.close();
    }
}
