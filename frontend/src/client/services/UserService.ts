/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { ForgotPasswordRequest } from '../models/ForgotPasswordRequest';
import type { LoginRequest } from '../models/LoginRequest';
import type { ResetPasswordRequest } from '../models/ResetPasswordRequest';
import type { Token } from '../models/Token';
import type { UserCreateRaw } from '../models/UserCreateRaw';
import type { UserRead } from '../models/UserRead';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class UserService {
    /**
     * Post User
     * @param requestBody
     * @returns UserRead Successful Response
     * @throws ApiError
     */
    public static postUserUserRegisterPost(
        requestBody: UserCreateRaw,
    ): CancelablePromise<UserRead> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/user/register',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Delete User
     * @param userId
     * @returns UserRead Successful Response
     * @throws ApiError
     */
    public static deleteUserUserUserIdDelete(
        userId: number,
    ): CancelablePromise<UserRead> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/user/{user_id}',
            path: {
                'user_id': userId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Read Users
     * Fetch all users.
     * @returns UserRead Successful Response
     * @throws ApiError
     */
    public static readUsersUserAllGet(): CancelablePromise<Array<UserRead>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/user/all',
        });
    }
    /**
     * Login
     * @param requestBody
     * @returns Token Successful Response
     * @throws ApiError
     */
    public static loginUserTokenPost(
        requestBody: LoginRequest,
    ): CancelablePromise<Token> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/user/token',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Forgot Password
     * @param requestBody
     * @returns any Successful Response
     * @throws ApiError
     */
    public static forgotPasswordUserForgotPasswordPost(
        requestBody: ForgotPasswordRequest,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/user/forgot-password',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Reset Password
     * @param requestBody
     * @returns any Successful Response
     * @throws ApiError
     */
    public static resetPasswordUserResetPasswordPost(
        requestBody: ResetPasswordRequest,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/user/reset-password',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
}
