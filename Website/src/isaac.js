import { createMuiTheme, ThemeProvider, makeStyles } from '@material-ui/core/styles';
import {Typography} from '@material-ui/core'; 
import NavBar from './components/NavBar'
import Grid from './components/Grid'
import Footer from './components/Footer'
import './App.css';
//changes to imports 
import SchoolIcon from '@material-ui/icons/School';
import AccountBalanceIcon from '@material-ui/icons/AccountBalance';
import ChildCareIcon from '@material-ui/icons/ChildCare';

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

function App() {
  const classes = styles(); 

  return (
    <div className="App">
      <ThemeProvider theme={theme}>
        <NavBar/>
        <div className={classes.wrapper}>
          <Typography variant="h4" className={classes.bigSpace} color="primary">
           Home
          </Typography>
          <Typography variant="h5" className={classes.littleSpace} color="primary">
          Welcome to SpeechEdTech! We help students of all ages improve their reading skills with the use of AI. Click one of the following buttons below to get feedback on your reading skills.
          </Typography>
        </div>
        <div className={`${classes.grid} ${classes.bigSpace}`}>
          <Grid icon={<ChildCareIcon style={{fill: "#4360A6", height:"125", width:"125"}}/>}  title="Kindergarten" btnTitle="Start Recording" />
          <Grid icon={<SchoolIcon style={{fill: "#449A76", height:"125", width:"125"}}/>} title="Primary" btnTitle="Start Recording"/>
          <Grid icon={<AccountBalanceIcon style={{fill: "#D05B2D", height:"125", width:"125"}}/>}  title="Secondary" btnTitle="Start Recording"/>
        </div>
        <div className={classes.bigSpace}>
        </div>
      </ThemeProvider>
    </div>
  );
}

export default App;
