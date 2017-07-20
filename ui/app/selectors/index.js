export const selectConfigurations = state => state.configurations;

export const selectExportRegion = (id, state) => state.hdx.exportRegions[id];

export const selectHDXError = state => state.hdx.error;

export const selectHDXStatus = state => state.hdx.status;

export const selectLocationOptions = state => state.hdx.locationOptions;

export const selectRuns = state => state.exportRuns;