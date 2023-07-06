import React, { useState } from 'react';

function Animal() {
  const joke = "Chuck Norris once kicked a horse in the chin. Its descendants are known as giraffes";
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
        <div className="kal">
          <h1>Animal</h1>
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

export default Animal;









