/*
 * flyteidl/service/admin.proto
 *
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * API version: version not set
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */

package flyteadmin

type EventTaskNodeMetadata struct {
	// Captures the status of caching for this execution.
	CacheStatus *EventCatalogCacheStatus `json:"cache_status,omitempty"`
	CatalogKey *EventCatalogMetadata `json:"catalog_key,omitempty"`
}