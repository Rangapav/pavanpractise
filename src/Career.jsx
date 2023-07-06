import React, { useState } from 'react';

function Career() {
  const joke = "Chuck Norris is actually the front man for Apple.He let's steve jobs run the show when he is on the mission,Norris is always on a mission ";
  const [buttonText, setButtonText] = useState('Next joke');
  const [showComponent, setShowComponent] = useState(true);


  const handleClick = () => {
    setButtonText('Next joke');
  };
  const handleClose = () => {
    setShowComponent(false);
  };

  return (
    <>
    {showComponent && (
    <div className='kal'> 
      <h1>Career </h1>
      <fieldset id="p">
      <p>{joke}</p>
      <button onClick={handleClick}>{buttonText}</button>
      <button className="close-button" onClick={handleClose}>
              &times;
            </button>
      </fieldset>
    </div>
    )}
    </>
  );
}

export default Career;








