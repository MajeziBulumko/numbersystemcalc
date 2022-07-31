import java.util.*;
import java.util.HashMap;

public class number_system_Calculator
{
   HashMap<String, char[]> my_dict = new HashMap<String, char[]>();
   public static void populateHash(){
     my_dict.put("hexa",{'0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'});
     my_dict.put("penta",{'0','1','2','3','4','5','6','7','8','9','a','b','c','d','e'});
     my_dict.put("tetra",{'0','1','2','3','4','5','6','7','8','9','a','b','c','d'});
     my_dict.put("trid",{'0','1','2','3','4','5','6','7','8','9','a','b','c'});
     my_dict.put("duo",{'0','1','2','3','4','5','6','7','8','9','a','b'});
     my_dict.put("unde",{'0','1','2','3','4','5','6','7','8','9','a'});
     my_dict.put("denary",{'0','1','2','3','4','5','6','7','8','9'});
     my_dict.put("nonary",{'0','1','2','3','4','5','6','7','8'});
     my_dict.put("octal",{'0','1','2','3','4','5','6','7'});
     my_dict.put("septe",{'0','1','2','3','4','5','6'});
     my_dict.put("senary",{'0','1','2','3','4','5'});
     my_dict.put("quin",{'0','1','2','3','4'});
     my_dict.put("quater",{'0','1','2','3'});
     my_dict.put("tern",{'0','1','2'});
     my_dict.put("bina",{'0','1'});

   }
   public static boolean are_numbers(String[] items)
   {
      boolean answer = true;
      for (int i = 0; i < items.length; i++){
        char[] ch = items[i].toCharArray();
        for (char it : ch ) {
          if (Character.isDigit(it)) {continue;}
          else {answer = false; break;}
        }
        if (answer) { continue; }
        else {break;}

      }
      return answer;
   }

   public static void rough_convert(int num, int base){
     if ((base > 16) && (base < 2)) {
       System.out.println("Numerical System not covered by this program yet.");
     }
     String[] bases = {"0","bina",
               "tern","quater",
               "quin","senary",
               "septe","octal",
               "nonary","denary",
               "unde","duo","trid",
               "tetra","penta","hexa"};
     String wrd_base = bases[base-1];
     char[] num_sys_arr = my_dict.get(wrd_base);
     String fin = "";
     Int cnt, temp;
     cnt = 0;
     while (cnt != num){
       temp = num % base;
       fin.concat(num_sys_arr[temp]);
       num = num / base;
     }
     System.out.println("0"+fin + " \nThat is your number in " + wrd_base );
     // figure out how to create and use dictinaries in Java
   }

   public static void calc(String[] item){
      if (are_numbers(item))
      {
        System.out.println("Was expecting numbers only");
        break;
      }
      Int num1,num1, count_system, fin;
      num1 = (int)item[0];
      num2 = (int)item[1];
      count_system = (int)item[2];
      fin = num1 + num2;
      rough_convert(fin, count_system);
   }

   public static void main(String[] args)
   {
      populateHash();
      System.out.println("Roses are red,");
      System.out.println("Violets are blue,");

   }
}
