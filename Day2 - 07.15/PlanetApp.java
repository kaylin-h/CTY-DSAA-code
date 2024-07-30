import java.util.Scanner;

public class PlanetApp(

    public static String [] planets;

    public static void main(String[] args){

        int M = 9;
        Scanner input = new Scanner(System.in);
        planets= new String[M];
        int menuChoice = 101;
        int FINISHED = 9; 
        itn level = -1;
        String newPlanetName;
        do{
            System.out.println("########");
            System.out.println("1. Enter 1 to add a planet to the list");
            System.out.println("2. Enter 2 to update a planet based on its ID");
            System.out.println("3. Enter 3 to display the number of planets available in the list");
            System.out.println("4. Enter 4 to delte a planet in the list");
            System.out.println("Enter " + FINISHED + " to end")
            System.out.println("########");
            menuChoice = input.nextInt(); //nextLine needs String while nextInt needs Int

            switch(menuChoice){
                case 1:
                    //grab a new planet name and add to the list 
                    System.out.println("Enter your new planet's name: ");
                    newPlanetName = input.next();
                    level += 1; //level = level + 1
                    planets[level] = newPlanetName;
                break;
                case 2:
                    //Ask for the ID of the planet to update
                    //then ask the new planets name, then update the item of the list at that index
                    System.out.println("Enter your planets ID to update: ");
                    int planetIndexToUpdate = input.nextInt();
                    if (planetIndexToUpdate >= 0 && planetIndexToUpdate <= level){

                        System.ou.println("Enter your new name for the current planet at index " + planetIndexToUpdate + " :")
                        newPlanetname = input.nextLine();
                        planets[planetIndexToUpdate] = newUpdateName;
                    }
                break;
                case FINISHED:
                    System.out.println("You are exiting the app");
            }

        }while(menuChoice != FINISHED);


    }
)