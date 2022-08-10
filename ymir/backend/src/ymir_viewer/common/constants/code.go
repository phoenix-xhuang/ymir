package constants

type ResponseCode int
type ResponseMsg string

const (
	ViewerSuccessCode ResponseCode = 0
	ViewerSuccessMsg  ResponseMsg  = "Success"

	FailDataMissCode ResponseCode = 180100
	FailDataMissMsg  ResponseMsg  = "Data not exist"

	FailInvalidParmsCode ResponseCode = 180101
	FailInvalidParmsMsg  ResponseMsg  = "Invalid parameters"
)