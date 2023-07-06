import React, { useState } from 'react';

function Movies() {
  const joke = "Chuck Norris once kicked a  horse in the chin. its decendants are known as giraffes";
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
      <h1>Movies </h1>
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

export default Movies;








