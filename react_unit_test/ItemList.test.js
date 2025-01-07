const ItemList = require("./itemList");

test("renders the correct number of items", () => {
  const items = ["Item 1", "Item 2", "Item 3"];
  const renderedItems = ItemList({ items });

  console.log(`Rendered items: ${renderedItems}`); // Debugging output
  expect(renderedItems.length).toBe(items.length);
});
