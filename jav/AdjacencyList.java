package jav;

import java.util.ArrayList;

public class AdjacencyList {
    private ArrayList<ArrayList<Integer>> map = new ArrayList<>();
    private boolean inverted = false;
    private boolean flipped = false;
    public AdjacencyList(int size){ for(int i = 0; i < size; i++){ addNode(); } }
    public void invert(){
        inverted = !inverted;
    }
    public void flip(){ flipped = !flipped; }
    public void addNode(){
        map.add(new ArrayList<>());
        if(inverted){
            int node = map.size()-1;
            for(ArrayList<Integer> as : map){ as.add(node); }
            for(int i = 0; i < map.size(); i++){ map.get(node).add(i); }
        }
    }
    public void addEdge(int src, int dest){
        int first = flipped?dest:src;
        int second = flipped?src:dest;
        if(inverted){
            map.get(first).remove((Integer)second);
        } else {
            map.get(first).add(second);
        }
    }
    public void delEdge(int src, int dest){
        int first = flipped?dest:src;
        int second = flipped?src:dest;
        if(inverted){
            map.get(first).add(second);
        } else {
            map.get(first).remove((Integer)second);
        }
    }
    public void delEdges(int node){
        if(inverted){
            map.set(node, new ArrayList<>());
            ArrayList<Integer> N=map.get(node);
            for(int i = 0; i < map.size(); i++){ N.add(i); }
            for(ArrayList<Integer> n : map){ if(!n.contains(node)){n.add(node);} }
        } else {
            map.set(node, new ArrayList<>());
            for(ArrayList<Integer> n : map){ n.remove((Integer)node); }
        }
    }
    public ArrayList<ArrayList<Integer>> rectify(boolean sideEffect){
        ArrayList<ArrayList<Integer>> temp = new ArrayList<>();
        for(int i = 0; i < map.size(); i++){
            temp.add(new ArrayList<>());
            for(int j = 0; j < map.size(); j++){
                if(i!=j&&(inverted^map.get(flipped?j:i).contains(flipped?i:j))){ temp.get(i).add(j); }
            }
            temp.get(i).sort((o1, o2) -> {return o1>o2?1:0;});
        }
        if(sideEffect){
            map = temp;
            flipped = false;
            inverted = false;
            return map;    
        }
        return temp;
    }
    public String toString(){
        ArrayList<ArrayList<Integer>> temp = rectify(false);
        ArrayList<ArrayList<Character>> string = new ArrayList<>();
        for(int i = 0; i < temp.size(); i++){                        
            for(int j = 0; j < temp.size(); j++){                    
                if(i==0){string.add(new ArrayList<>());}            
                string.get(i).add(temp.get(i).contains(j)?'.':'x');  
            }
        }
        String res = ""+(flipped?"F":"")+(inverted?"I":"")+"\n";
        for(ArrayList<Character> cs : string){
            for(char c : cs){ res+=c; }
            res+='\n';
        }
        return res;
    }
    public int nodeCount(){ return map.size(); }
    /** Rectify prior to hashing */
    public String nodeHash(int node){
        ArrayList<Integer> out = map.get(node);
        long hash = 0;
        int count = out.size();
        for(int i = 0; i < out.size(); i++){
            hash+=Math.pow(7,i)*out.get(i);
            while(hash>=1000000007){ hash-=1000000007; }
        }
        return count+" "+hash;
    }
}
