public class number_system_Calculator
{
   public static are_numbers(String[] items)
   {
      boolean answer = true;
      for (int i = 0; i < items.length; i++){
        if (items[i]).isdigit() continue;
        else answer = false; break;
      }
      return answer;
   }

   public static void rough_convert(int num, int base){
     if (base > 16) && (base < 2) {
       System.out.println("Numerical System not covered by this program yet.")
     }
     // figure out how to create and use dictinaries in Java
   }

   public static void main(String[] args)
   {
      System.out.println("Roses are red,");
      System.out.println("Violets are blue,");
   }
}
