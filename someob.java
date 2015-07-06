/*
 * @David Torrejon
 * Solucio als 2 problemes plantejats per ob al test d'entrada per incidental
 */
package oneboxapply;

/**
 *
 * @author User
 */
public class OneBoxApply {

    /*
    ** solve_first: given a integer say if its base 2. 2,4,8,16,32
    */
    
    public Boolean solve_First(int n){
        int i=2; 
        while(n%i==0 ){
            if(n==2) return true;
            n=n/2;
        }
        System.out.println(n);
        return false;
    }
    /*
    ** Given a string say if it has more than 50% MAYUS, and if it does 
    ** print all MAYUS, else all MINUS
    */
    public Boolean solve_Second(String somechain){
        int counterMayus = 0;
        int counterMinus = 0;
        int asciiDif = 97-65;
        for (int i=0;i<somechain.length();i++){
            if(somechain.charAt(i)<91) counterMayus++;
            else counterMinus++;
        }
        if(counterMayus>counterMinus){    
            for (int i=0;i<somechain.length();i++){
                if(somechain.charAt(i)>91) somechain=somechain.replace(somechain.charAt(i), (char)(somechain.charAt(i)-asciiDif));
            }
        }else {
            for (int i=0;i<somechain.length();i++){
                if(somechain.charAt(i)<91) somechain=somechain.replace(somechain.charAt(i), (char)(somechain.charAt(i)+asciiDif));
            }
        }
        System.out.println(somechain);
        return false;
    }
    
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        OneBoxApply obA = new OneBoxApply();
        System.out.println(obA.solve_First(128));
        System.out.println(obA.solve_Second("hoLaASDssdsdasdEEAGHHDFG"));
    
    }
    
}
