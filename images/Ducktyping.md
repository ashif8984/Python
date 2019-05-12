# Duck Typing

## Explanation 1:
Discussion of the semantics of the question is fairly nuanced (and very academic), but here's the general idea:

(“If it walks like a duck and quacks like a duck then it is a duck.”) 
- YES! but what does that mean??! This is best illustrated by example:

 ### Example: Dynamically typed languages

Imagine I have a **magic wand**. It has special powers. If I wave the wand and say "Drive!" to a car, well then, it drives!
Does it work on other things? Not sure: so I try it on a truck. Wow - it drives too! I then try it on planes, trains and 1 Woods (they are a type of golf club which people use to 'drive' a golf ball). They all drive!

But would it work on say, a teacup? Error: KAAAA-BOOOOOOM! that didn't work out so good. ====> Teacups can't drive!! duh!?

This is basically the concept of duck typing. It's a try-before-you-buy system. If it works, all is well. But if it fails, well, it's gonna blow up in your face.

In other words, we are interested in ***what the object can do, rather than with what the object is***.

### Example: statically typed languages

If we were concerned with what the object actually was, then our magic trick will work only on pre-set, authorised types - in this case cars, but will fail on other objects which can drive: trucks, mopeds, tuk-tuks etc. It won't work on trucks because our magic wand is expecting it to only work on cars.

In other words, in this scenario, the magic wand looks very closely at what the object is (is it a car?) rather than what the object can do (e.g. whether cars, trucks etc. can drive).

The only way you can get a truck to drive is if you can somehow get the magic wand to expect both trucks and cars (perhaps by "implementing a common interface"). If you don't know what that means then just ignore it for the moment.

**Summary: Key take-out***

What's important in duck typing is ***what the object can actually do, rather than what the object is.

## Explanation 2:
Consider you are designing a simple function, which gets an object of type Bird and calls its **walk()** method. There are two approaches, that you can think of:

1. This is my function and I must be sure that what it only accepts the Bird, or their code will not compile. If anyone wants to use my function, he must be aware that I only accept Bird

1. My function get any objects and I just call the object walk() method. So, if the object can walk() it is correct, if it can't my function will fails. So here it is not important the object is a Bird or anything else, it is important that it can walk() (This is duck typing)
It must be considered that the duck typing may be useful in some cases, for example Python uses duck typing a lot
