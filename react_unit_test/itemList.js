function ItemList({ items }) {
    return items.map((item, index) => `<li key=${index}>${item}</li>`);
  }
  
  module.exports = ItemList;
  