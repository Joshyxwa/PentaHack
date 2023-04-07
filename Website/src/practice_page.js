import React, { Component , useState,useEffect }  from 'react';
import { createMuiTheme, ThemeProvider, makeStyles } from '@material-ui/core/styles';
import {Box,Typography} from '@material-ui/core'; 
import NavBar from './components/NavBar'
import Grid from './components/Grid'
import Footer from './components/Footer'
import RecordButton from './components/recording'
import './App.css';
//changes to imports 
import SecurityIcon from '@material-ui/icons/Security';
import EventNoteIcon from '@material-ui/icons/EventNote';
import TrendingUpIcon from '@material-ui/icons/TrendingUp';
import ImportExportIcon from '@material-ui/icons/ImportExport';
import ComputerIcon from '@material-ui/icons/Computer';
import HttpIcon from '@material-ui/icons/Http';


const theme = createMuiTheme({
  palette: {
    primary: {
      main:"#2e1667",
    },
    secondary: {
      main:"#c7d8ed",
    },
  },
  typography: {
    fontFamily: [
      'Roboto'
    ],
    h4: {
      fontWeight: 600,
      fontSize: 28,
      lineHeight: '2rem',
      },
    h5: {
      fontWeight: 100,
      lineHeight: '2rem',
    },
  },
});

const styles = makeStyles({
  wrapper: {
    width: "65%",
    margin: "auto",
    textAlign: "center"
  },
  bigSpace: {
    marginTop: "5rem"
  },
  littleSpace:{
    marginTop: "2.5rem",
  },
  grid:{
    display: "flex", 
    justifyContent: "center",
    alignItems: "center",
    flexWrap: "wrap", 
  },
})

function Practice() {
  const classes = styles();
  const [questions, setQuestions] = useState([]);
  const [selectedPassage, setSelectedPassage] = useState('');
  const level = localStorage.getItem('level');
  console.log(level)
  useEffect(() => {
    // Fetch data from the endpoint using localStorage value as a condition
    fetch(`/questions/${level}`,{
      method:'GET'
    })

      .then((response) => response.json())
      
      .then((data) => setQuestions(data))
      
      .catch((error) => console.log(error));
  }, [level]);
  console.log(questions)
  const handlePassageSelection = (passage) => {
    setSelectedPassage(passage);
  };

  return (
    <div className="App">
      <ThemeProvider theme={theme}>
        <NavBar />
        <div className={classes.wrapper}>
          <Typography variant="h4" className={classes.bigSpace} color="primary">
            Reading Aloud
          </Typography>
     
            <Typography variant="h5" className={classes.littleSpace} color="primary">
              Once upon a time, there was a curious little mouse. One day, the mouse went on an adventure to find some cheese. On the way, the mouse met a friendly cat who showed him the way. Together, they found a big block of cheese and shared it happily. The end.
            </Typography>
          
          <RecordButton />
   
          <Typography variant="h4" className={classes.bigSpace} color="primary">
            Transcribe Text
          </Typography>
          <Typography variant="h5" className={classes.littleSpace} color="primary">
           
           </Typography>
                    <Box
            border={4}
            borderRadius={16}
            borderColor="primary.main"
            display="flex"
            justifyContent="center"
          >
        
          <Typography variant="h5" className={classes.littleSpace} color="primary">
            Once  a time there was a curious little mouse One say the mouse went on an adventure to find some cheese On the day the mouse met a friendly cat who showed him the way Together they found a big block of cheese and shared it happily The end
          </Typography>
        </Box>
        </div>
      </ThemeProvider>
    </div>
  );
}



export default Practice;
