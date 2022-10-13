/* eslint-disable no-unused-vars */
import SalesView from "../views/sales/SalesView.vue";
import DailySalesView from "../views/sales/DailySalesView.vue";
import NewSaleView from "../views/sales/NewSaleView.vue";
import SaleDetailsView from "../views/sales/SaleDetailsView.vue";

export default [
  {
    path: "/sales",
    name: "sales",
    component: SalesView,
    meta: {
      title: "Sales",
      breadcrumb: [
        {
          text: (route) => "Sales",
          to: "sales",
          active: true,
        },
      ],
    },
  },
  {
    path: "/sales/daily",
    name: "daily-sales",
    component: DailySalesView,
    meta: {
      title: "Sales",
      breadcrumb: [
        {
          text: (route) => "Sales",
          to: "sales",
          active: false,
        },
        {
          text: (route) => "Daily Sales",
          to: "daily-sales",
          active: true,
        },
      ],
    },
  },
  {
    path: "/sales/new-sale",
    name: "new-sale",
    component: NewSaleView,
    meta: {
      title: "New Sale",
      breadcrumb: [
        {
          text: (route) => "Sales",
          to: "sales",
          active: false,
        },
        {
          text: (route) => "New Sale",
          to: "new-sale",
          active: true,
        },
      ],
    },
  },
  {
    path: "/sales/:saleId",
    name: "sale-view",
    component: SaleDetailsView,
    meta: {
      title: "Sale Details",
      breadcrumb: [
        {
          text: (route) => "Sales",
          to: "sales",
          active: false,
        },
        {
          text: (route) => "Daily Sales",
          to: "daily-sales",
          active: false,
          query: true,
        },
        {
          text: (route) => `${route.meta.title}`,
          to: "sale-view",
          active: true,
        },
      ],
    },
  },
];