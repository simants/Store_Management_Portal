import { Avatar, Box, Card, CardContent, Grid, LinearProgress, Typography } from "@mui/material";
import InsertChartIcon from "@mui/icons-material/InsertChartOutlined";

export const TasksProgress = (props) => {
  const returns = parseInt(props.blockValues.profit_loss);

  return (
    <Card sx={{ height: "100%" }} {...props}>
      <CardContent>
        <Grid container spacing={3} sx={{ justifyContent: "space-between" }}>
          <Grid item>
            <Typography color="textSecondary" gutterBottom variant="overline">
              P / L
            </Typography>
            <Typography color="textPrimary" variant="h4">
              {returns > 1000 ? parseInt(returns / 1000).toString() + "k" : returns}
            </Typography>
          </Grid>
          <Grid item>
            <Avatar
              sx={{
                backgroundColor: "warning.main",
                height: 56,
                width: 56,
              }}
            >
              <InsertChartIcon />
            </Avatar>
          </Grid>
        </Grid>
        {/* <Box sx={{ pt: 3 }}>
          <LinearProgress value={75.5} variant="determinate" />
        </Box> */}
      </CardContent>
    </Card>
  );
};
