package Introduction;

public class Control_Statements {
    public static void main(String[] args) {
        int x=120;
        int y=122;
        int z=60;
        if (x > y && x > z)
          System.out.println(x);
        else if(y > z)
          System.out.println(y);
        else
          System.out.println(z);

          int a = 1;
          switch(a){
              case 0:
                    System.out.println("Sunday");
                    break;
              case 1:
                    System.out.println("Monday");
                    break;
                case 2:
                    System.out.println("Tuesday");
                    break;
                default:
                    System.out.println("AnyDay");
          }
          a = 4;
          switch(a){
              case 0:
              case 6:
                    System.out.println("Weekend");
                    break;
              case 1:
              case 2:
              case 3:
              case 4:
              case 5:
                     System.out.println("Weekday");
                     break;
              default:
                    System.out.println("Wrong Day");
          }
        }
      }