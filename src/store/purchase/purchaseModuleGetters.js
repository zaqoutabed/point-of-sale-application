export default {
  getPurchasesList: (state) => state.purchases.data,
  getPurchasesPagination: (state) => state.purchases.pagination,
  getPurchaseDetails: (state) => state.purchase,
};