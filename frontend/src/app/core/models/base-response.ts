export interface BaseResponse<T> {
  success: boolean;
  message: string;
  data: T;
}

export interface PaginatedResponse<T> {
  items: T[];
  total: number;
  page: number;
  size: number;
  pages: number;
}

export interface ErrorDetail {
  field: string;
  msg: string;
}

export interface ErrorResponse {
  success: boolean;
  message: string;
  errors: ErrorDetail[];
}
