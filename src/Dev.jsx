import React, { useState } from 'react';

function Dev() {
  const joke = "Chuck Norris can't test for equality because he has no equal.";
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
      <h1>Dev </h1>
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

export default Dev;








