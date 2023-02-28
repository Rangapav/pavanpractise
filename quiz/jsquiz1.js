(function() {
  var questions = [{
    question: " Javascript is an _______ language?",
    choices:["Object-Oriented","Object-base","Procedural","None Of the above"],
    correctAnswer:0      
  },{
    question: "What will be the output of the following code snippet? a = [1, 2, 3, 4, 5];print(a.slice(2, 4));",
    choices: ["3,4" ,"1,2,3", "3,4,5", "2,3,4"],
    correctAnswer: 0
  }, {
    question: "Which function is used to serialize an object into a JSON string in Javascript?",
    choices: ["parse()","convert()",'stringify()',"N/A"],
    correctAnswer: 2
  }, {
    question:'What will be the output of the following code snippet?print(typeof(NaN));',
    choices : ["object","string","Number","N/A"],
    correctAnswer: 2
  }, {
    question: "What is 8*8?",
    choices: [20, 30, 40, 50, 64],
    correctAnswer: 4
  },{
    question: "How many districts in new formation of Andhra Pradesh?",
    choices: [13,25,26,29,15],
    correctAnswer: 2
  },{
    question: "How many friends does pavan had?",
  choices: [02,04,06,08,10],
  correctAnswer: 2
  },{
    question: "What is your course Period?",
  choices: [04,05,06,08,10],
  correctAnswer: 2
  },{
    question: "When did India mens Cricket team won first one-day world cup?",
  choices: [1980,1981,1983,1984,1985],
  correctAnswer: 3
  },{
    question: "in which couse are you doing?",
  choices: ["python","java","c++","html&css","php"],
  correctAnswer: 0
  },{
    question:"who is the primeminister of india?",
    choices:["N Modi","Amit Shah","Jai shankar","venkayaNaidu"],
    correctAnswer:0
    },{question:"who is the president of india?",
    choices:["N Modi","D Murma","Jai shankar","Sarojini Naidu"],
    correctAnswer:0
    },{question:"who is the chiefminister of AndhraPradesh?",
    choices:["N Modi","jagan","chandrababu","venkayaNaidu"],
    correctAnswer:1
    },{question:"who is the  cpatian of indian cricket team?",
    choices:["R Sharma","v kohli","kl Rahul","Bumrah"],
    correctAnswer:0
  
  }];
  
  var questionCounter = 0; //Tracks question number
  var selections = []; //Array containing user choices
  var quiz = $('#quiz'); //Quiz div object
  
  // Display initial question
  displayNext();
  
  // Click handler for the 'next' button
  $('#next').on('click', function (e) {
    e.preventDefault();
    
    // Suspend click listener during fade animation
    if(quiz.is(':animated')) {        
      return false;
    }
    choose();
    
    // If no user selection, progress is stopped
    if (isNaN(selections[questionCounter])) {
      alert('Please make a selection!');
    } else {
      questionCounter++;
      displayNext();
    }
  });
  
  // Click handler for the 'prev' button
  $('#prev').on('click', function (e) {
    e.preventDefault();
    
    if(quiz.is(':animated')) {
      return false;
    }
    choose();
    questionCounter--;
    displayNext();
  });
  
  // Click handler for the 'Start Over' button
  $('#start').on('click', function (e) {
    e.preventDefault();
    
    if(quiz.is(':animated')) {
      return false;
    }
    questionCounter = 0;
    selections = [];
    displayNext();
    $('#start').hide();
  });
  
  // Animates buttons on hover
  $('.button').on('mouseenter', function () {
    $(this).addClass('active');
  });
  $('.button').on('mouseleave', function () {
    $(this).removeClass('active');
  });
  
  // Creates and returns the div that contains the questions and 
  // the answer selections
  function createQuestionElement(index) {
    var qElement = $('<div>', {
      id: 'question'
    });
    
    var header = $('<h2>Question ' + (index + 1) + ':</h2>');
    qElement.append(header);
    
    var question = $('<p>').append(questions[index].question);
    qElement.append(question);
    
    var radioButtons = createRadios(index);
    qElement.append(radioButtons);
    
    return qElement;
  }
  
  // Creates a list of the answer choices as radio inputs
  function createRadios(index) {
    var radioList = $('<ol>');
    var item;
    var input = '';
    for (var i = 0; i < questions[index].choices.length; i++) {
      item = $('<li>');
      input = '<input type="radio" name="answer" value=' + i + ' />';
      input += questions[index].choices[i];
      item.append(input);
      radioList.append(item);
    }
    return radioList;
  }
  
  // Reads the user selection and pushes the value to an array
  function choose() {
    selections[questionCounter] = +$('input[name="answer"]:checked').val();
  }
  
  // Displays next requested element
  function displayNext() {
    quiz.fadeOut(function() {
      $('#question').remove();
      
      if(questionCounter < questions.length){
        var nextQuestion = createQuestionElement(questionCounter);
        quiz.append(nextQuestion).fadeIn();
        if (!(isNaN(selections[questionCounter]))) {
          $('input[value='+selections[questionCounter]+']').prop('checked', true);
        }
        
        // Controls display of 'prev' button
        if(questionCounter === 1){
          $('#prev').show();
        } else if(questionCounter === 0){
          
          $('#prev').hide();
          $('#next').show();
        }
      }else {
        var scoreElem = displayScore();
        quiz.append(scoreElem).fadeIn();
        $('#next').hide();
        $('#prev').hide();
        $('#start').show();
      }
    });
  }
  
  // Computes score and returns a paragraph element to be displayed
  function displayScore() {
    var score = $('<p>',{id: 'question'});
    
    var numCorrect = 0;
    for (var i = 0; i < selections.length; i++) {
      if (selections[i] === questions[i].correctAnswer) {
        numCorrect++;
      }
    }
    
    score.append('You got ' + numCorrect + ' questions out of ' +
                 questions.length + ' right!!!');
    return score;
  }
 
  
})();