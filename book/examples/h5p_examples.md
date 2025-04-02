# Examples of H5p Quizzes

## Dialog cards

Dialog cards can be used to ask open questions about the content students are reading or, more intrestingly, to check the conclusion the students draw from the interactive exercises built into the book.

**Engineering Systems Optimization**

A great example of this can be found in the book: Engineering Systems Optimization. [Chapter 4](https://teachbooks.io/engineering-systems-optimization/2023/pages/moo_example.html) called Mulit-objective optimization has an in depth sub-chapter which is used to compare the relation between engine power and emissions and how to optimize for both.

```{figure} figures/Live_code.PNG
---
width: 600
align: center
---
Problem Statement
```

As can be seen on the right-hand-side menu, the sub-chapter includes the problem statement, the elaboration on the model and solution method and finally an exercise for the student. The code in the page is activated by pressing the live code button which will make the code cells editable and executable. Additionally, interactive figures are included into the text with movable sliders to directly see the effect of the changes made.

```{iframe} ../_static/power.html
:height: 580px
:width: 100%
```

The H5p quizzes can shine in the section on questions, discussions and comments. Next to many multiple choice questions (which are discussed later) there are dialog cards which can ask more conceptual and open ended questions. Pressing on the blue button `Turn` will flip around the card and reveal the model answer. The great thing about the integration of both interactive aspects (coding and questions) helps the student to play around with the code and understand the topic from a less theoretical point-of-view.

```{h5p} https://tudelft.h5p.com/content/1292260184374358717/embed
```

```{h5p} https://tudelft.h5p.com/content/1292260188487459217/embed
```


## Question Set 

Question sets consist of a question and one or more possible answers to that question.

**MUDE - Observation Theory**

The following question sets are taken from chapter 3.3. Weighted least-squares estimation of the MUDE 23/24 book. The chapter builds on the previous chapter on simple least-squares estimation and dwelves into the importance and properties of the weight matrix. The student is primarily quizzed using multiple choice questions to check their understanding. The answers can be provided in the shape of text, figures, equations, matrices and probably much more.

```{h5p} https://tudelft.h5p.com/content/1292060781042105617/embed
```

```{h5p} https://tudelft.h5p.com/content/1292046737060674407/embed
```

Since these questions are meant to develop the understanding of the students, feedback is vital! Feedback can be built into the questions to explain the reasoning behind a correct answer.

```{figure} figures/Question_set_3.PNG
---
width: 600
align: center
---
Correct Answer Feedback
```
And when the answer is not correct, tips can be given to nudge the student towards the right solution.

```{figure} figures/Question_set_4.PNG
---
width: 600
align: center
---
Tips
```
**Try it out!**

Have a look at the following 7 questions.

```{h5p} https://tudelft.h5p.com/content/1292062157562749767/embed
```

## Complex fill in the blanks

The complex fill in the blanks can be used to evaluate numerical answers. 

**MUDE - Observation Theory**

Chapter 3.7. Non-linear least-squares estimation from the MUDE 23/24 book makes use of the complex fill in the blanks quiz in order to check that the students understood the composition of the Jacobian Matrix specifically used in deriving the linearized functional model. This model is essential for accurately estimating values and assessing system behavior of complex processes that arent linear. 

```{h5p} https://tudelft.h5p.com/content/1292064774866067777/embed
```
As you can see, the precision of the answer sought for is specified and the figure below shows again the incorporation of feedback.

```{figure} figures/blanks2.PNG
---
width: 600
align: center
---
Wrong Answer + Feedback
```

**MUDE - Optimization**

Since the cells can be used to evaluate numerical answers, they are an easy way to quiz the student on matrices and evaluate the result of each position independently. The optimization team of MUDE took this a step further and used this set-up to quiz the students on the SIMPLEX method. This method automates the solving of the augmented form of a linear programming problem with continuous variables. It makes use of tables and the manipulation of equations to find the optimal values. Unfortunately, with a large number of variables this tables tend to get quite big and filling in the cells becomes laborious.

```{h5p} https://tudelft.h5p.com/content/1292131432784432037/embed
```
**Truss structure**

Truss structures are modelled as rigid bars (so elements which cannot deform) connected by hinges (so elements can rotate with respect to one each other). In our model, hinges are indicate with a circle, and bars with a line. For example, the structure you've seen in the second example (with two diagonal bars removed) is modelled as follows:

```{figure} ../images/Truss1.svg
:name: truss structure

Bars and hinges in truss structure
```

Now that you've been introduced to truss structures, answer the following question:

```{h5p} https://tudelft.h5p.com/content/1291910926067816717/embed
```

## True or False 

This next type of quiz is fairly self explainatory :)

**MUDE - Optimization**

Once again the chapter on [optimization](https://mude.citg.tudelft.nl/book/optimization/sand_and_clay.html#lp-formulation-of-the-problem) in the MUDE book integrated many true and false questions to test the students on the problem statement which, like in many engineering problems, is just as important if not more important than the solution procedure. This is especially when the case when small tweaks to the equations, such as seen in the figure below, can change the result of the optimization drastically. 

```{figure} figures/truefalse0.PNG
---
width: 600
align: center
---
Problem Statement
```

The small circles below the question indicates that there are more questions in this series which can be viewed by clicking on the blue arrow pointing towards the left or right. Open the second, fourth and fifth question:

```{h5p} https://tudelft.h5p.com/content/1292120485436114287/embed
```

**Try it out!**

```{h5p} https://tudelft.h5p.com/content/1292061623388939257/embed
```

## Drag and Drop

Drag and Drop questions are useful to make the distinction between different concepts that might often cause confusion.

**MUDE - Optimization**

In this chapter, it was important that the students made the distinction between the terminology and mathematical meaning between different elements of the graphical solution method. A drag and drop question was used to link the term to its definition. The answer boxes can be dragged to the correct title in a playful manner.

The fourth question in this question set is a drag and drop question:

```{h5p} https://tudelft.h5p.com/content/1292121213033110307/embed
```

The correct answer leads to:

```{figure} figures/drag2.PNG
---
width: 600
align: center
---
Solution
```