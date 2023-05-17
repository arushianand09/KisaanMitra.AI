import React from 'react';
import './Cards.css';
import CardItem from './CardItem';

function Cards() {
  return (
    <div className='cards'>
      <h1>Unlock a World of Farming Services with KisaanMitraa.AI - Let's Grow Together!</h1>
      <div className='cards__container'>
        <div className='cards__wrapper'>
          <ul className='cards__items'>
            <CardItem
              src='images/img-9.jpg'
              text='Plant Disease Detector'
               label='AI'
              path='/plantdisease'
            />
            <CardItem
              src='images/img-2.jpg'
              text='Chat Assistant'
               label='AI'
              path='/chatbot'
            />
          </ul>
          <ul className='cards__items'>
            <CardItem
              src='images/img-3.jpg'
              text='Real Time Weather Updates'
               label='API'
              path='/weather'
            />
            <CardItem
              src='images/img-4.jpg'
              text='Smart Irrigation System'
               label='AI'
              path='/products'
            />
            { <CardItem
              src='images/img-8.jpg'
              text='Coming Soon'
              // label='Adrenaline'
              path='/sign-up'
            /> }
          </ul>
        </div>
      </div>
    </div>
  );
}

export default Cards;
