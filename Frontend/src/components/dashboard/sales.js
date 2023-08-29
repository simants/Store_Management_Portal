import { Bar } from "react-chartjs-2";
import {
  Box,
  Button,
  Card,
  CardContent,
  CardHeader,
  Select,
  Divider,
  useTheme,
  MenuItem,
} from "@mui/material";
import ArrowDropDownIcon from "@mui/icons-material/ArrowDropDown";
import ArrowRightIcon from "@mui/icons-material/ArrowRight";
import { useState } from "react";

export const Sales = (props) => {
  const theme = useTheme();

  const [val, setVal] = useState(7);

  const handleDaysChange = (e) => {
    const days = e.target.value;
    setVal(days);
    props.salesParentCallback(days)
  };

  const sales = props.salesValues;

  // function findAllByKey(obj, keyToFind) {
  //   return (
  //     Object.entries(obj).reduce(
  //       (acc, [key, value]) =>
  //         key === keyToFind
  //           ? acc.concat(value)
  //           : typeof value === "object" && value
  //           ? acc.concat(findAllByKey(value, keyToFind))
  //           : acc,
  //       []
  //     ) || []
  //   );
  // }

  const data = {
    datasets: [
      {
        backgroundColor: "#3F51B5",
        barPercentage: 0.5,
        barThickness: 12,
        borderRadius: 4,
        categoryPercentage: 0.5,
        data: Object.values(sales),
        label: "This year",
        maxBarThickness: 10,
      },
    ],
    labels: Object.keys(sales),
  };

  const options = {
    animation: false,
    cornerRadius: 20,
    layout: { padding: 0 },
    legend: { display: false },
    maintainAspectRatio: false,
    responsive: true,
    xAxes: [
      {
        ticks: {
          fontColor: theme.palette.text.secondary,
        },
        gridLines: {
          display: false,
          drawBorder: false,
        },
      },
    ],
    yAxes: [
      {
        ticks: {
          fontColor: theme.palette.text.secondary,
          beginAtZero: true,
          min: 0,
        },
        gridLines: {
          borderDash: [2],
          borderDashOffset: [2],
          color: theme.palette.divider,
          drawBorder: false,
          zeroLineBorderDash: [2],
          zeroLineBorderDashOffset: [2],
          zeroLineColor: theme.palette.divider,
        },
      },
    ],
    tooltips: {
      backgroundColor: theme.palette.background.paper,
      bodyFontColor: theme.palette.text.secondary,
      borderColor: theme.palette.divider,
      borderWidth: 1,
      enabled: true,
      footerFontColor: theme.palette.text.secondary,
      intersect: false,
      mode: "index",
      titleFontColor: theme.palette.text.primary,
    },
  };

  return (
    <Card {...props}>
      <CardHeader
        action={
          <Select
            labelId="demo-simple-select-standard-label"
            id="demo-simple-select-standard"
            value={val}
            label="Age"
            sx={{ color: "darkviolet", fontSize: "small", fontWeight: "bold", outline: "0" }}
            onChange={handleDaysChange}
          >
            <MenuItem value={7} sx={{ color: "darkviolet", fontSize: "small", fontWeight: "bold" }}>
              Last 7 days
            </MenuItem>
            <MenuItem
              value={15}
              sx={{ color: "darkviolet", fontSize: "small", fontWeight: "bold" }}
            >
              Last 15 days
            </MenuItem>
            <MenuItem value={0} sx={{ color: "darkviolet", fontSize: "small", fontWeight: "bold" }}>
              This month
            </MenuItem>
          </Select>
        }
        title="Latest Sales"
      />
      <Divider />
      <CardContent>
        <Box
          sx={{
            height: 400,
            position: "relative",
          }}
        >
          <Bar data={data} options={options} />
        </Box>
      </CardContent>
      <Divider />
      <Box
        sx={{
          display: "flex",
          justifyContent: "flex-end",
          p: 2,
        }}
      >
        <Button color="primary" endIcon={<ArrowRightIcon fontSize="small" />} size="small">
          Overview
        </Button>
      </Box>
    </Card>
  );
};

const _sales = {
  1: {
    category_details: [
      {
        product_category: "category_name",
        sale: "00000",
      },
      {
        product_category: "category_name",
        sale: "00000",
      },
    ],
    total_sales: "23100",
  },

  2: {
    category_details: [
      {
        product_category: "category_name",
        sale: "00000",
      },
      {
        product_category: "category_name",
        sale: "00000",
      },
    ],
    total_sales: "23400",
  },

  3: {
    category_details: [
      {
        product_category: "category_name",
        sale: "00000",
      },
      {
        product_category: "category_name",
        sale: "00000",
      },
    ],
    total_sales: "23000",
  },
};
