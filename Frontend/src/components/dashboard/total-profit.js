import { Avatar, Card, CardContent, Grid, Typography } from "@mui/material";
import GradeRoundedIcon from '@mui/icons-material/GradeRounded';

export const TotalProfit = (props) => {
  const rating = props.blockValues.rating;
  return (
    <Card {...props}>
      <CardContent>
        <Grid container spacing={3} sx={{ justifyContent: "space-between" }}>
          <Grid item>
            <Typography color="textSecondary" gutterBottom variant="overline">
              Rating
            </Typography>
            <Typography color="textPrimary" variant="h4">
              {rating}
            </Typography>
          </Grid>
          <Grid item>
            <Avatar
              sx={{
                backgroundColor: "primary.main",
                height: 56,
                width: 56,
              }}
            >
              <GradeRoundedIcon />
            </Avatar>
          </Grid>
        </Grid>
      </CardContent>
    </Card>
  );
};
