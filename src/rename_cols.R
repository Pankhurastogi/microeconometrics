rename_columns <- function(data2, column_mapping) {
  # Loop through the column mapping dictionary
  for (key in names(column_mapping)) {
    # Rename columns in data2 based on the mapping
    colnames(data2)[colnames(data2) == column_mapping[[key]]] <- key
  }
  # Return the modified data2
  return(data2)
}
