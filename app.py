{"Doanh_thu": "{:,.0f} VNĐ"}
                    ),
                    use_container_width=True,
hide_index=True,
                )

            st.markdown("---")

            # Phân tích biến động doanh thu theo tháng
            st.write("### 📅 Doanh thu bán hàng theo Tháng")
            df_anal["Tháng_Số"] = df_anal["Thời gian"].dt.month
            summary_thang = (
                df_anal.groupby(["Tháng_Số", "Tháng-Năm"])
                .agg(
                    Số_lượng_bán=("Số lượng", "sum"),
                    Doanh_thu=("Thành tiền", "sum"),
                )
                .reset_index()
                .sort_values("Tháng_Số")
            )

            col_chart3, col_table3 = st.columns([1.5, 1])
            with col_chart3:
                st.write("**Biểu đồ cột tăng trưởng doanh thu qua các tháng:**")
                st.bar_chart(summary_thang.set_index("Tháng-Năm")["Doanh_thu"])
            with col_table3:
                st.write("**Tổng doanh thu chi tiết từng tháng:**")
                st.dataframe(
                    summary_thang[
                        ["Tháng-Năm", "Số_lượng_bán", "Doanh_thu"]
                    ].style.format({"Doanh_thu": "{:,.0f} VNĐ"}),
                    use_container_width=True,
                    hide_index=True,
                )
        else:
            st.info(
                "Chưa có dữ liệu giao dịch để thống kê. Hãy tiến hành thanh toán một vài đơn hàng trước."
            )
