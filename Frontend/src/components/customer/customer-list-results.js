import { useEffect, useState } from "react";
import PerfectScrollbar from "react-perfect-scrollbar";
import PropTypes from "prop-types";
import { format } from "date-fns";
import { DataGrid, GridToolbar } from "@mui/x-data-grid";
import {
  Avatar,
  Box,
  Card,
  Checkbox,
  Table,
  TableBody,
  TableCell,
  TableHead,
  TablePagination,
  TableRow,
  Typography,
  useTheme,
} from "@mui/material";
import Rating from "@mui/material/Rating";
import { Bar, Line } from "react-chartjs-2";
import { Button, CardContent, TextField, InputAdornment, SvgIcon } from "@mui/material";
import { Search as SearchIcon } from "../../icons/search";
import { getInitials } from "../../utils/get-initials";

export const CustomerListResults = ({
  params,
  employeeRatings,
  paymentData,
  productData,
  lossReportData,
  busyHourData,
  ...rest
}) => {
  
  useEffect(() => {
    // getData();
  }, []);

  const [selectedCustomerIds, setSelectedCustomerIds] = useState([]);
  const [limit, setLimit] = useState(10);
  const [page, setPage] = useState(0);

  const theme = useTheme();

  const columns = [
    { field: "store", headerName: "Store", flex: 1 },
    {
      field: "employee_name",
      headerName: "Employee",
      flex: 1,
      editable: true,
    },
    {
      field: "average_rating",
      headerName: "Rating",
      sortable: false,
      flex: 1,
      renderCell: (params) => {
        return (
          <strong>
            <Rating name="read-only" value={params.row.average_rating} readOnly />
          </strong>
        );
      },
      //
    },
  ];

  const rows = employeeRatings;

  const data_1 = {
    datasets: [
      {
        backgroundColor: "#3F51B5",
        barPercentage: 0.5,
        barThickness: 12,
        borderRadius: 4,
        categoryPercentage: 0.5,
        data: paymentData.Cash,
        label: "Cash",
        maxBarThickness: 10,
      },
      {
        backgroundColor: "crimson",
        barPercentage: 0.5,
        barThickness: 12,
        borderRadius: 4,
        categoryPercentage: 0.5,
        data: paymentData.Card,
        label: "Card",
        maxBarThickness: 10,
      },
    ],
    labels: paymentData.Store,
  };

  const data_2 = {
    datasets: [
      {
        backgroundColor: "#3F51B5",
        barPercentage: 0.5,
        barThickness: 12,
        borderRadius: 4,
        categoryPercentage: 0.5,
        data: productData.Local,
        label: "Local",
        maxBarThickness: 10,
      },
      {
        backgroundColor: "crimson",
        barPercentage: 0.5,
        barThickness: 12,
        borderRadius: 4,
        categoryPercentage: 0.5,
        data: productData.Brand,
        label: "Brand",
        maxBarThickness: 10,
      },
    ],
    labels: productData.Store,
  };

  const colors = ["crimson", "violet", "blue", "lightblue", "pink"];

  const prepareData = (data) => {
    const keys_array = Object.keys(data);
    const data_3 = {
      datasets: [],
      labels: [],
    };
    keys_array.forEach((key, idx) => {
      const element = data[key];
      const loss_value_list = [];
      const label_list = [];
      element.forEach((item) => {
        loss_value_list.push(item.loss_damage_quantity);
        label_list.push(item.product_category);
      });
      const data_object = {
        backgroundColor: colors[idx],
        barPercentage: 0.5,
        barThickness: 12,
        borderRadius: 4,
        categoryPercentage: 0.5,
        data: loss_value_list,
        label: key,
        maxBarThickness: 10,
      };
      data_3.datasets.push(data_object);
      data_3.labels.push(label_list);
    });
    data_3.labels = data_3.labels[0];
    // console.log(data_3);
    return data_3;
  };

  const prepareBusyHourData = (data) => {
    console.log("BH", data);

    const keys_array = Object.keys(data);

    const morning = [];
    const afternoon = [];
    const night = [];

    keys_array.forEach((key, idx) => {
      const element = data[key];
      morning.push(element["6-12"]);
      afternoon.push(element["12-18"]);
      night.push(element["18-24"]);
    });

    const data_4 = {
      datasets: [
        {
          backgroundColor: colors[4],
          barPercentage: 0.5,
          barThickness: 12,
          borderRadius: 4,
          categoryPercentage: 0.5,
          data: morning,
          label: "Morning",
          maxBarThickness: 10,
        },
        {
          backgroundColor: colors[2],
          barPercentage: 0.5,
          barThickness: 12,
          borderRadius: 4,
          categoryPercentage: 0.5,
          data: afternoon,
          label: "Afternoon",
          maxBarThickness: 10,
        },
        {
          backgroundColor: colors[1],
          barPercentage: 0.5,
          barThickness: 12,
          borderRadius: 4,
          categoryPercentage: 0.5,
          data: night,
          label: "Night",
          maxBarThickness: 10,
        }
      ],
      labels: keys_array,
    };

    console.log(data_4);

    return data_4;
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
    <Card {...rest}>
      <PerfectScrollbar>
        <Box sx={{ width: "100%", height: 300 }}>
          <DataGrid
            sx={{ textAlign: "center" }}
            rows={rows}
            columns={columns}
            pageSize={10}
            getRowId={(row) => row.employee_name}
            disableColumnMenu={true}
            onCellEditStop={(params, event) => {
              console.log(params.row);
              console.log(event.target.value);
            }}
          />
        </Box>
        <CardContent sx={{ display: "inline-flex" }}>
          <Box
            sx={{
              height: 400,
              width: 500,
              margin: 2,
            }}
          >
            <h3 style={{ textAlign: "center" }}>Payment Analysis</h3>
            <Bar data={data_1} options={options} />
          </Box>
          <Box
            sx={{
              height: 400,
              width: 500,
              margin: 2,
            }}
          >
            <h3 style={{ textAlign: "center" }}>Product Analysis</h3>
            <Bar data={data_2} options={options} />
          </Box>
        </CardContent>
        <CardContent sx={{ display: "inline-flex" }}>
          <Box
            sx={{
              height: 400,
              width: 500,
              margin: 2,
            }}
          >
            <h3 style={{ textAlign: "center" }}>Loss Report</h3>
            <Line data={prepareData(lossReportData)} options={options} />
          </Box>
          <Box
            sx={{
              height: 400,
              width: 500,
              margin: 2,
            }}
          >
            <h3 style={{ textAlign: "center" }}>Busy Hour Analysis</h3>
            <Bar data={prepareBusyHourData(busyHourData)} options={options} />
          </Box>
        </CardContent>
      </PerfectScrollbar>
    </Card>
  );
};

CustomerListResults.propTypes = {
  customers: PropTypes.array.isRequired,
};

// import * as React from 'react';
// import { DataGrid } from '@mui/x-data-grid';

// export default function DataGridDemo() {
//   return (
//     <div style={{ height: 400, width: '100%' }}>
//       <DataGrid
//         rows={rows}
//         columns={columns}
//         pageSize={5}
//         rowsPerPageOptions={[5]}
//         checkboxSelection
//         disableSelectionOnClick
//       />
//     </div>
//   );
// }
