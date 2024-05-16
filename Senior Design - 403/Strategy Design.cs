////////////////////////////////////////////////////////////////////////////////////////////
// Name: Norman Cook
// Date: 10/21/2020
// Description: Implementation of the strategy design pattern using an animal super class,
//      a bird subclass, a dog subclass, and a dynamic method for whether or not the animal
//      can fly.
////////////////////////////////////////////////////////////////////////////////////////////
using System;

namespace StrategyDesignPattern
{
    class Strategy
    {
        // entry point
        static void Main(string[] args)
        {
            // create two new animals, a dog and bird
            Dog dog1 = new Dog();
            Bird bird1 = new Bird();
            
            // Dog1 Properties
            // set a name and speed for the dog
            // set the method type for this animal's ability to fly
            dog1.setName("Clifford");
            dog1.setSpeed(10);
            dog1.setFlyingAbility(FlightType.Ground);

            // Bird1 Properties
            // set a name and speed for the bird
            // set the method type for this animal's ability to fly
            bird1.setName("Tweety");
            bird1.setSpeed(50);
            bird1.setFlyingAbility(FlightType.Flight);

            // display each animal's name and ability to fly
            Console.WriteLine(dog1.getName());
            Console.WriteLine(dog1.tryToFly());
            Console.WriteLine();
            Console.WriteLine(bird1.getName());
            Console.WriteLine(bird1.tryToFly());
        }
    }

    // animals have a name, speed value, and a flying capability
    public class Animal
    {
        private string name;
        private double speed;

        // getters and setters for name and speed
        public void setName(string newName)
        {
            name = newName;
        }

        public string getName()
        {
            return name;
        }

        public void setSpeed(double newSpeed)
        {
            speed = newSpeed;
        }
        public double getSpeed()
        {
            return speed;
        }

        // object variable that determines which flying type the animal has
        private FlightType _flightType;

        // constructor for animal
        public Animal()
        {

        }

        // setter for changing the flying type for the animal
        public void setFlyingAbility(FlightType flightType)
        {
            _flightType = flightType;
        }

        // getter for trying to fly
        // return the appropriate class from the interface when flight is attempted
        public string tryToFly()
        {
            IFlys FlyRequest;

            switch (_flightType)
            {
                case FlightType.Flight:
                    FlyRequest = new DoesFly();
                    return FlyRequest.animalFly();
                case FlightType.Ground:
                    FlyRequest = new DoesNotFly();
                    return FlyRequest.animalFly();
            }

            return null;
        }
    }

    // interface that references a method for returning 
    // a string about the animal's flight ability
    public interface IFlys
    {
        string animalFly();
    }

    // Two Strategy Classes that inherit from the interface
    // These classes determine which method will be selected based 
    // on whether or not the animal can fly.
    public class DoesFly : IFlys
    {
        public string animalFly()
        {
            return "Flying High!";
        }
    }

    public class DoesNotFly : IFlys
    {
        public string animalFly()
        {
            return "I can't fly.";
        }
    }

    // user defined type for which flight the animal is capable of
    public enum FlightType
    {
        Flight = 1,
        Ground = 2
    }

    // two subclasses that iherit from the animal class for a dog and bird
    public class Dog : Animal
    { }

    public class Bird : Animal
    { }
}
