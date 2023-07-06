import React, { useState } from 'react';

function Celebrity() {
  const joke = "Chuck Norris smells what the Rock is cooking... because the Rock is chuck Norris' personal chef.";
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
      <h1>Celebrity</h1>
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

export default Celebrity;








