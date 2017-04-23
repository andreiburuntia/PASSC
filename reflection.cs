using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using System.Text;
using System.Threading.Tasks;

namespace passc_reflection
{
   class Program
   {
      static void Main(string[] args)
      {
         Assembly a = Assembly.LoadFile(@"C:\Users\andre\OneDrive\Documents\Visual Studio 2015\Projects\ClassLibrary1\ClassLibrary1\bin\Debug\ClassLibrary1.dll");
         foreach (Type type in a.GetTypes())
         {
            Console.WriteLine(type.FullName);
            if (type.IsClass)
            {
               Console.WriteLine("is class");
               if (type.IsPublic)
               {
                  Console.WriteLine("is public");
               }
               if (type.IsAbstract)
               {
                  Console.WriteLine("is abstract");
               }

               Console.WriteLine();

               Console.WriteLine("implements the following interfaces:");

               foreach (var intfs in type.GetInterfaces())
               {
                  Console.WriteLine(intfs);
               }
               if (type.BaseType != null)
               {
                  Console.WriteLine("extends " + type.BaseType);
               }

               Console.WriteLine();

               Console.WriteLine("has the following fields:");

               foreach (FieldInfo field in type.GetFields(BindingFlags.Instance |
                                                          BindingFlags.Static |
                                                          BindingFlags.Public |
                                                          BindingFlags.NonPublic))
               {
                  if (field.IsPrivate)
                     Console.WriteLine(field.Name + " - " + field.FieldType + " - private");
                  if (field.IsPublic)
                     Console.WriteLine(field.Name + " - " + field.FieldType + " - public");
               }

               Console.WriteLine();
               Console.WriteLine("has the following constructors:");

               foreach (ConstructorInfo constructor in type.GetConstructors(BindingFlags.Instance |
                                                          BindingFlags.Static |
                                                          BindingFlags.Public |
                                                          BindingFlags.NonPublic))
               {
                  Console.WriteLine(constructor.Name + " - args: ");
                  foreach (ParameterInfo pi in constructor.GetParameters())
                  {
                     Console.WriteLine(pi.ParameterType);
                  }
               }

               Console.WriteLine();
               Console.WriteLine("has the following methods:");

               foreach (MethodInfo method in type.GetMethods(BindingFlags.Instance |
                                                          BindingFlags.Static |
                                                          BindingFlags.Public |
                                                          BindingFlags.NonPublic))
               {
                  Console.WriteLine(method.Name + " - returns " + method.ReturnType + " - args: ");
                  foreach (ParameterInfo pi in method.GetParameters())
                  {
                     Console.WriteLine(pi.ParameterType);
                  }
               }
            }
            if (type.IsInterface)
            {
               Console.WriteLine("is interface");
            }

            Console.WriteLine("--------------------");
            Console.WriteLine();
            Console.WriteLine();
            Console.WriteLine("--------------------");
         }
         Console.ReadLine();
      }
   }
}
